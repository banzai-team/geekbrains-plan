import axios from "axios";
import { config } from "~/config/config";

// export type UploadFilePayload = {
//   file: any;
// };

// export async function uploadFile(payload: UploadFilePayload) {
//   const form = new FormData();
//   form.append("file", payload.file);
//
//   return await axios.post(`${config.apiUrl}/api/plan/pdf`, form, {
//     headers: {
//       'Content-Type': `multipart/form-data;`,
//     },
//   });
// }

export async function uploadLink(payload: any) {
  return await axios.post(`${config.apiUrl}/plan`, {
    url: payload.link
  }, {
    headers: {
      'Content-Type': `application/json;`,
    },
  });
}