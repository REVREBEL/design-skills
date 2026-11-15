// Illustrative React/TanStack Table starter, not a production-verified grid.
import { useMemo } from "react";
import { ColumnDef, flexRender, getCoreRowModel, useReactTable } from "@tanstack/react-table";

type PropertyRow = { id: string; name: string; occupancy: number | null; adr: number | null; revpar: number | null; currency: string };
const percent = (value: number | null) => value == null ? "N/A" : new Intl.NumberFormat(undefined,{ style:"percent", minimumFractionDigits:1, maximumFractionDigits:1 }).format(value);
const money = (value: number | null, currency: string) => value == null ? "N/A" : new Intl.NumberFormat(undefined,{ style:"currency", currency }).format(value);
export function RevenueGrid({ rows }: { rows: PropertyRow[] }) {
  const columns = useMemo<ColumnDef<PropertyRow>[]>(() => [
    { accessorKey: "name", header: "Property" },
    { accessorKey: "occupancy", header: "Occupancy", cell: ({row}) => <span className="block text-right font-numeric-tabular">{percent(row.original.occupancy)}</span> },
    { accessorKey: "adr", header: "ADR", cell: ({row}) => <span className="block text-right font-numeric-tabular">{money(row.original.adr,row.original.currency)}</span> },
    { accessorKey: "revpar", header: "RevPAR", cell: ({row}) => <span className="block text-right font-numeric-tabular">{money(row.original.revpar,row.original.currency)}</span> },
  ], []);
  const table = useReactTable({ data:rows, columns, getCoreRowModel:getCoreRowModel(), getRowId: row=>row.id });
  return <div className="overflow-x-auto"><table className="w-full text-sm"><caption className="sr-only">Property performance, with N/A for unavailable measures</caption><thead>{table.getHeaderGroups().map(g=><tr key={g.id}>{g.headers.map(h=><th scope="col" className="p-2 text-left" key={h.id}>{flexRender(h.column.columnDef.header,h.getContext())}</th>)}</tr>)}</thead><tbody>{table.getRowModel().rows.map(row=><tr key={row.id}>{row.getVisibleCells().map(cell=><td className="p-2" key={cell.id}>{flexRender(cell.column.columnDef.cell,cell.getContext())}</td>)}</tr>)}</tbody></table></div>;
}
