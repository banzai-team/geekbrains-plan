import Head from '~/components/Head';

function Page404() {
  return (
    <>
      <Head title="The page is not found" />
      <div>
        <h1>The page is not found.</h1>
        <a href="/">Top Page</a>
      </div>
    </>
  );
}

export default Page404;
