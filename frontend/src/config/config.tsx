declare global {
  interface Window {
    API_URL?: string;
  }
}

export const config = {
  apiUrl: "http://api.geekbrains.banzai-predict.site:4000/api"
}