import React from 'react';
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from '~/components/ui/breadcrumb';
import { Link } from 'react-router-dom';

type BreadcrumbsProps = {
  path: { text: string; link: string }[];
};

const Breadcrumbs: React.FC<BreadcrumbsProps> = ({ path }) => {
  return (
    <Breadcrumb className="hidden md:flex pb-4">
      <BreadcrumbList>
        {path.map((item, key) => {
          const isLast = path.length === key + 1;

          return (
            <>
              <BreadcrumbItem key={`path-${key}`}>
                <BreadcrumbLink asChild={!isLast}>
                  {!isLast ? <Link to={item.link}>{item.text}</Link> : <BreadcrumbPage>{item.text}</BreadcrumbPage>}
                </BreadcrumbLink>
              </BreadcrumbItem>
              {!isLast ? <BreadcrumbSeparator /> : null}
            </>
          );
        })}
      </BreadcrumbList>
    </Breadcrumb>
  );
};

export default Breadcrumbs;
