export async function likeVacancy(url: string) {
  const result = fetch("https://api.restful-api.dev/objects", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url,
    }),
  });

  return result;
}
