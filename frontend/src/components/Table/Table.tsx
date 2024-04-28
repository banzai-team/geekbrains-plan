import React from 'react';
import { useNavigate } from 'react-router';

import { Badge } from '~/components/ui/badge';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '~/components/ui/table';
import { Routes } from '~/pages/Router';
import {File, Trash2} from 'lucide-react';
import { Button } from '~/components/ui/button';

{
  /*TODO: check real data*/
}

type TableRow = {
  id: string;
  source: string;
  sourceType: "pdf" | "url"
  response: any;
  performedAt: string;
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

  const onDelete = (event: any, id: string) => {
    event.stopPropagation();
    event.preventDefault();
    console.log('delete ', id);
    // delete(row.id);
  };

  return (
    <Table>
      <TableHeader>
        <TableHead className="text-left">Вакансия</TableHead>
        <TableHead className="text-left">Курс</TableHead>
        <TableHead className="text-left">Направление</TableHead>
        <TableHead className="text-left">Уровень</TableHead>
        <TableHead className="text-left">Дата</TableHead>
        <TableHead className="text-left">Работа модели</TableHead>
        <TableHead className="text-right" />
      </TableHeader>
      <TableBody>
        {data.map((item) => (
          <TableRow onClick={() => onRowClick(item?.id)} key={`table-row-${item?.id}`} className="text-left">
            <TableCell className="max-w-40 overflow-hidden text-ellipsis whitespace-nowrap">
              <a
                  onClick={(event) => {
                    event.stopPropagation();
                  }}
                  href={item?.source}
                  target="_blank"
                  className="font-medium hover:text-primary"
              >
                {item?.sourceType === 'pdf' ? <File /> : item?.source}
                </a>
            </TableCell>
            <TableCell className="max-w-48 w-max overflow-hidden text-ellipsis whitespace-nowrap">
              <a
                  onClick={(event) => {
                    event.stopPropagation();
                  }}
                  href={item?.response?.eduCourses[0]?.program?.url}
                  target="_blank"
                  className="font-medium hover:text-primary"
              >
                {item?.response?.eduCourses[0]?.program?.name}
              </a>
            </TableCell>
            <TableCell>
              {item?.response?.eduCourses[0]?.program?.tag}
            </TableCell>
            <TableCell>
              {item?.response?.eduCourses[0]?.program?.difficulty}
            </TableCell>
            <TableCell className="w-20">
              {new Date(item?.performedAt)?.toLocaleDateString("ru-RU")}
            </TableCell>
            <TableCell className="w-36 max-w-48 whitespace-nowrap text-center">
              <Badge className="text-xs" variant={!item?.source ? 'destructive' : item?.response?.eduCourses?.length ? 'default' : 'secondary'}>
                {!item?.source ? 'Ошибка' : item?.response?.eduCourses?.length ? 'Готово' : 'В процессе'}
              </Badge>
            </TableCell>
            <TableCell className="text-right w-10">
              <Button variant="ghost" size="sm" onClick={(e) => onDelete(e, item?.id)}>
                <Trash2 className="w-4 h-4 text-destructive" />
              </Button>
            </TableCell>
          </TableRow>
        )).reverse()}
      </TableBody>
    </Table>
  );
};

export default MainTable;
