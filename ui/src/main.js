import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import VueSweetalert2 from "vue-sweetalert2";
import "sweetalert2/dist/sweetalert2.min.css";

const app = createApp(App);
app.config.globalProperties = {
  API_URL: `http://${window.location.hostname}:8081/api/`,
};

app.use(router);
app.use(createPinia());
app.use(VueSweetalert2);

app.mount("#app");
