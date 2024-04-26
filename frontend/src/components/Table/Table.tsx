import React from 'react';
import { useNavigate } from 'react-router';

import { Badge } from '~/components/ui/badge';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '~/components/ui/table';
import { Routes } from '~/pages/Router';
import { Trash2 } from 'lucide-react';
import { Button } from '~/components/ui/button';

{
  /*TODO: check real data*/
}
type TableRow = {
  id: string;
  vacancy: string;
  vacancyLink: string;
  price: string;
  status: string;
};

type MainTableProps = {
  data: TableRow[];
};

const MainTable: React.FC<MainTableProps> = ({ data }) => {
  const navigate = useNavigate();

  const onRowClick = (id: string) => {
    navigate(`${Routes.Vacancy}/${id}`);
  };

  const onDelete = (event, id) => {
    event.stopPropagation();
    event.preventDefault();
    console.log('delete ', id);
    // delete(row.id);
  };

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
        {data.map((item) => (
          <TableRow onClick={() => onRowClick(item.id)} key={`table-row-${item.id}`}>
            <TableCell>
              <a
                onClick={(event) => {
                  event.stopPropagation();
                }}
                href={item.vacancyLink}
                target="_blank"
                className="font-medium hover:text-primary"
              >
                {item.vacancy}
              </a>
            </TableCell>
            <TableCell className="hidden sm:table-cell">
              {/*TODO: FIX variant if we will have status*/}
              <Badge className="text-xs" variant={item.status === 'Done' ? 'default' : 'secondary'}>
                {item.status}
              </Badge>
            </TableCell>
            <TableCell className="text-right">{item.price}</TableCell>
            <TableCell className="text-right">
              <Button variant="ghost" size="sm" onClick={(e) => onDelete(e, item.id)}>
                <Trash2 className="w-4 h-4 text-destructive" />
              </Button>
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
};

export default MainTable;
