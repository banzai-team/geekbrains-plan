import axios from "axios";
import { request, gql } from "graphql-request";

import { config } from "~/config/config";


const ModelsQuery = gql`
    query modelRequests {
        modelRequests {
            id
            performedAt
            response {
                eduCourses {
                    id
                    program {
                        daysAmount
                        difficulty
                        id
                        name
                        price
                        speciality
                        tag
                        url
                    }
                }
                simularCourses {
                    id
                    matchScore
                    program {
                        daysAmount
                        difficulty
                        id
                        name
                        price
                        speciality
                        tag
                        url
                        modules {
                            id
                            title
                        }
                    }
                }
                meta
            }
            source
            sourceType
        }
    }
`;

const ModelQuery = gql`
    query modelRequest($id: Int!) {
        modelRequest(id: $id) {
            id
            performedAt
            extractedText
            response {
                eduCourses {
                    id
                    program {
                        daysAmount
                        difficulty
                        id
                        name
                        price
                        speciality
                        tag
                        url
                    }
                }
                simularCourses {
                    id
                    matchScore
                    program {
                        daysAmount
                        difficulty
                        id
                        name
                        price
                        speciality
                        tag
                        url
                        modules {
                            id
                            title
                        }
                    }
                }
                meta
            }
            source
            sourceType
            extractedText
        }
    }
`;


export async function getRequests() {
  const response = await request<{ modelRequests: any }>(`${config.apiUrl}/graphql`, ModelsQuery, {});
  return response.modelRequests;
}

export async function getRequest(id: string) {
  const response = await request<{ modelRequest: any }>(`${config.apiUrl}/graphql`, ModelQuery, {id: Number.parseInt(id)});
  return response.modelRequest;
}

export type UploadFilePayload = {
  file: any;
};

export async function uploadFile(payload: UploadFilePayload) {
  const form = new FormData();
  form.append("file", payload.file);

  return await axios.post(`${config.apiUrl}/api/plan/pdf`, form, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
}

export async function uploadLink(payload: any) {
  return await axios.post(`${config.apiUrl}/api/plan`, {
    url: payload.link
  }, {
    headers: {
      'Content-Type': `application/json;`,
    },
  });
}