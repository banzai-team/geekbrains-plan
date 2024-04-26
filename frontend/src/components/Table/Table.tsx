import React from "react";

import { Badge } from "~/components/ui/badge"
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "~/components/ui/table"

{/*TODO: check real data*/}
type TableRow = {
  vacancy: string;
  vacancyLink: string;
  price: string;
  status: string;
};

type MainTableProps = {
  data: TableRow[]
};

const MainTable: React.FC<MainTableProps> = ({data}) => {
    return (
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Вакансия</TableHead>
            <TableHead className="hidden sm:table-cell">Статус</TableHead>
            <TableHead className="text-right">Цена</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {
            data.map((item, key) => (
                <TableRow>
                  <TableCell>
                    <a href={item.vacancyLink} target="_blank" className="font-medium hover:text-primary">{item.vacancy}</a>
                  </TableCell>
                  <TableCell className="hidden sm:table-cell">
                      {/*TODO: FIX variant if we will have status*/}
                    <Badge className="text-xs" variant={item.status === "Done" ? "default" : "secondary"}>
                      {item.status}
                    </Badge>
                  </TableCell>
                  <TableCell className="text-right">{item.price}</TableCell>
                </TableRow>
            ))
          }
        </TableBody>
      </Table>
    );
}

export default MainTable;