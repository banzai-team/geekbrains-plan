import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { CardContent, CardFooter } from '~/components/ui/card';
import { Input } from '~/components/ui/input';
import { Button } from '~/components/ui/button';

const validationSchema = Yup.object({
  link: Yup.string().test(function (value) {
    const { file } = this.parent;
    if (!file) return value != null;
    return true;
  }),
  file: Yup.string().test(function (value) {
    const { link } = this.parent;
    if (!link) return value != null;
    return true;
  }),
});

type AddVacancyFormProps = {
  onSubmit: (values: { link?: string; file?: string }) => void;
};

const AddVacancyForm: React.FC<AddVacancyFormProps> = ({ onSubmit }) => {
  const formik = useFormik<{
    link: string;
    file: string;
  }>({
    initialValues: {
      link: '',
      file: '',
    },
    onSubmit: async (values) => onSubmit(values),
    validationSchema,
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <CardContent className="grid gap-4 sm:grid-cols-1 md:grid-cols-2">
        <div>
          <Input
            placeholder="Файл в процессе"
            {...formik.getFieldProps('file')}
            disabled={!!formik.values.link || true}
          />
        </div>

        <div>
          <Input placeholder="Ссылка" {...formik.getFieldProps('link')} disabled={!!formik.values.file} />
        </div>
      </CardContent>

      <CardFooter className="justify-end">
        <Button type="submit" disabled={!formik.isValid}>
          Добавить
        </Button>
      </CardFooter>
    </form>
  );
};

export default AddVacancyForm;
