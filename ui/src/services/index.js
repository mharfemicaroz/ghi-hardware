import axios from "axios";
import { useAuthStore } from "@/stores/authStore";
import { createPinia } from "pinia";
import { createApp } from "vue";
import App from "../App.vue";

const pinia = createPinia();
const app = createApp(App);
app.use(pinia);

const windowLocation = window.location;
const BASE_URL = `http://${windowLocation.hostname}:8081/api/`;

const authStore = useAuthStore();
const user = authStore.user;
const token = user ? user.token : null;
const author = user ? user.username : null;

const AUTH_HEADER = `Token ${token}`;

const makeRequest = async (method, url, data = {}) => {
  try {
    const { data: responseData } = await axios({
      method,
      url: `${BASE_URL}${url}`,
      data,
      headers: { Authorization: AUTH_HEADER },
    });
    return responseData;
  } catch (error) {
    console.error("Error:", error);
    throw error;
  }
};

export const fetchAllItems = async (url) => {
  return makeRequest("get", url);
};

export const fetchItem = async (url, id) => {
  return makeRequest("get", `${url}${id}`);
};

export const addItem = async (url, data) => {
  data.author = author;
  return makeRequest("post", url, data);
};

export const editItem = async (url, id, data) => {
  return makeRequest("put", `${url}${id}/`, data);
};

export const deleteItem = async (url, id) => {
  return makeRequest("get", `${url}delete/${id}`);
};

export const filterItems = async (url, data) => {
  return makeRequest("post", `${url}filter/`, data);
};

export const saveImage = async (data) => {
  return makeRequest("post", "savefile/", data);
};
