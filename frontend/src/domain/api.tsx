import axios from "axios";
import { request, gql } from "graphql-request";

import { config } from "~/config/config";


const ModelsQuery = gql`
    query modelRequests {
        modelRequests {
            id
            eduCourses {
                eduCourse
            }
            performedAt
            request
        }
    }
`;

const ModelQuery = gql`
    query modelRequest($id: String!) {
        modelRequest(id: $id) {
            id
            eduCourses {
                eduCourse
            }
            performedAt
            request
        }
    }
`;


export async function getRequests() {
  const response = await request<{ modelRequests: any }>(`${config.apiUrl}/graphql`, ModelsQuery, {});
  return response.modelRequests;
}

export async function getRequest(id: string) {
  const response = await request<{ modelRequest: any }>(`${config.apiUrl}/graphql`, ModelQuery, {});
  return response.modelRequest;
}

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
  return await axios.post(`${config.apiUrl}/api/plan`, {
    url: payload.link
  }, {
    headers: {
      'Content-Type': `application/json;`,
    },
  });
}