# Tailwind Form Layout Patterns

Use these as implementation patterns, not as a replacement for the host project's design system.

## 1. Constrained Form Shell

Keep the form readable instead of stretching fields across the viewport.

```tsx
<form className="mx-auto w-full max-w-2xl space-y-10">
  ...
</form>
```

If the surrounding page already owns the max width, do not add a second arbitrary constraint.

## 2. Field Anatomy

Labels remain visible. Helper/error text sits below the control.

```tsx
<div className="space-y-2">
  <label
    htmlFor="email"
    className="block text-sm font-medium text-foreground"
  >
    Email address
  </label>

  <input
    id="email"
    name="email"
    type="email"
    autoComplete="email"
    className="min-h-11 w-full rounded-md border border-input bg-background px-3 py-2 text-foreground outline-none transition focus-visible:ring-2 focus-visible:ring-ring"
  />

  <p className="text-sm text-muted-foreground">
    We'll send the confirmation here.
  </p>
</div>
```

For an error state, replace or supplement helper text with an associated error message and appropriate semantics.

## 3. Two Related Fields

Use grid when paired fields should align.

```tsx
<div className="grid grid-cols-1 gap-5 sm:grid-cols-2">
  <Field name="firstName" />
  <Field name="lastName" />
</div>
```

Do not force two columns merely because the viewport is wide enough.

## 4. Mixed-Width Address Group

Use column spans to reflect expected content length.

```tsx
<div className="grid grid-cols-1 gap-5 md:grid-cols-6">
  <div className="min-w-0 md:col-span-6">
    <Field name="address1" />
  </div>

  <div className="min-w-0 md:col-span-3">
    <Field name="city" />
  </div>

  <div className="min-w-0 md:col-span-1">
    <Field name="state" />
  </div>

  <div className="min-w-0 md:col-span-2">
    <Field name="postalCode" />
  </div>
</div>
```

The exact spans are contextual. Preserve logical reading/tab order.

## 5. Form Section Without Card Overuse

Use typography and spacing before reaching for a card.

```tsx
<section className="space-y-6">
  <div className="space-y-1">
    <h2 className="text-lg font-semibold text-foreground">
      Guest details
    </h2>
    <p className="text-sm text-muted-foreground">
      Tell us who will be checking in.
    </p>
  </div>

  <div className="space-y-5">
    ...
  </div>
</section>
```

For a stronger boundary:

```tsx
<section className="space-y-6 border-t border-border pt-8">
  ...
</section>
```

Use a background/card only when that boundary carries real meaning.

## 6. Inline Choice Group

For compact controls such as radio-like choices:

```tsx
<fieldset className="space-y-3">
  <legend className="text-sm font-medium text-foreground">
    Arrival method
  </legend>

  <div className="flex flex-wrap gap-3">
    ...
  </div>
</fieldset>
```

Allow wrapping. Do not squeeze labels into unreadable fixed widths.

## 7. Action Row

```tsx
<div className="flex flex-col-reverse gap-3 pt-4 sm:flex-row sm:items-center sm:justify-end">
  <button type="button" className="...secondary...">
    Back
  </button>
  <button type="submit" className="...primary...">
    Continue
  </button>
</div>
```

`flex-col-reverse` can preserve a useful mobile emphasis when the primary action should appear first visually while keeping intentional source order. Use only when keyboard/screen-reader order remains appropriate for the task.

## 8. Error State

```tsx
<div className="space-y-2">
  <label htmlFor="phone" className="block text-sm font-medium">
    Phone number
  </label>

  <input
    id="phone"
    aria-invalid="true"
    aria-describedby="phone-error"
    className="min-h-11 w-full rounded-md border border-destructive bg-background px-3 py-2 focus-visible:ring-2 focus-visible:ring-destructive"
  />

  <p id="phone-error" className="text-sm text-destructive">
    Enter a valid phone number.
  </p>
</div>
```

The exact tokens must come from the project. Do not invent `destructive`, `ring`, etc. if the project uses different names.

## 9. Read-Only Summary Group

Avoid styling read-only values like disabled inputs when they are not editable.

```tsx
<dl className="grid grid-cols-1 gap-x-6 gap-y-4 sm:grid-cols-2">
  <div>
    <dt className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
      Check-in
    </dt>
    <dd className="mt-1 text-sm text-foreground">Oct 12, 2026</dd>
  </div>
</dl>
```

Use inputs only when the value is actually editable or needs form semantics.

## 10. Responsive Rules

Prefer a small number of meaningful transformations:

```tsx
<div className="
  grid grid-cols-1 gap-5
  md:grid-cols-2
  xl:gap-6
">
  ...
</div>
```

Good responsive changes:
- 1 column → 2 columns
- stacked actions → inline actions
- compact page padding → larger page padding
- full-width form → constrained max width

Suspicious responsive changes:
- different field order at every breakpoint
- arbitrary width percentages per screen size
- five or more breakpoint-specific overrides on one field group
- changing the visual grouping so much that desktop and mobile feel like different forms

## 11. Tailwind Class Discipline

Prefer:
- existing semantic tokens
- existing component variants
- `gap-*` for sibling relationships
- grid spans for field width
- responsive prefixes for structural changes
- `min-w-0` where long content could overflow a grid/flex child

Avoid:
- repeated `mt-*` on every child to simulate a spacing system
- raw hex values when tokens exist
- `style={{ width: ... }}` for normal responsive layout
- fixed heights for fields containing wrapping content
- arbitrary widths such as `w-[43%]` unless reproducing an intentional measured design
- hiding labels and relying on placeholders
- `overflow-hidden` around fields when it clips focus rings or errors

## 12. Tailwind Version Awareness

Before using version-specific syntax:
1. inspect `package.json`
2. inspect Tailwind config / CSS entrypoint
3. follow the project's established syntax
4. do not migrate Tailwind versions as a side effect of a form task

Tailwind v4 projects may rely more heavily on CSS-first tokens and theme variables. Tailwind v3 projects commonly keep more configuration in `tailwind.config.*`. Preserve whichever architecture the host project already uses.

## 13. Pre-Ship Sweep

Search the edited form for:
- arbitrary colors
- arbitrary spacing
- duplicated class strings
- inline responsive styles
- missing `focus-visible`
- labels with no associated control
- error text detached from the field
- cramped multi-column layouts
- controls below practical touch height
- inconsistent section spacing

Fix the pattern, not just the individual symptom.
