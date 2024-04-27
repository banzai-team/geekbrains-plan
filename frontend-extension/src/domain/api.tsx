import { config } from "~/config/config.tsx";

export async function likeVacancy(url: string) {
  const result = fetch(`${config.apiUrl}/api/plan`, {
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
