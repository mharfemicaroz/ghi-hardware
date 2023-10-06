<template>
  <div class="main-wrapper">
    <div class="account-content">
      <form @submit.prevent="login">
        <div class="login-wrapper">
          <div class="login-content">
            <div class="login-userset">
              <div class="login-logo">
                <img src="/img/logo.png" alt="img" />
              </div>
              <div class="login-userheading">
                <h3>Sign In</h3>
                <h4>Please login to your account</h4>
              </div>
              <div class="form-login">
                <label>Username</label>
                <div class="form-addons">
                  <input
                    type="text"
                    placeholder="Enter your username"
                    v-model="username"
                    :readonly="isAuthenticated"
                  />
                  <img src="/img/icons/users1.svg" alt="img" />
                </div>
              </div>
              <div class="form-login">
                <label>Password</label>
                <div class="pass-group">
                  <input
                    type="password"
                    class="pass-input"
                    placeholder="Enter your password"
                    v-model="password"
                    :readonly="isAuthenticated"
                  />
                  <span class="fas toggle-password fa-eye-slash"></span>
                </div>
              </div>

              <div class="form-login">
                <button
                  type="submit"
                  class="btn btn-login"
                  :disabled="isAuthenticated"
                >
                  Sign In
                </button>
              </div>
            </div>
          </div>
          <div class="login-img">
            <img src="/img/login.jpg" alt="img" />
          </div>
        </div>
      </form>
    </div>
  </div>
  <ToasterComponent ref="toast" />
</template>
<script>
import ToasterComponent from "../common/ToasterComponent.vue";
import { useAuthStore } from "@/stores/authStore"; // Import the authStore
import Swal from "sweetalert2";
export default {
  components: {
    ToasterComponent,
  },
  data() {
    return {
      username: "",
      password: "",
      isAuthenticated: false,
    };
  },
  methods: {
    async login() {
      const authStore = useAuthStore(); // Access the authStore
      const authAccess = await authStore.login({
        username: this.username,
        password: this.password,
      });
      if (authAccess) {
        this.isAuthenticated = true;
        localStorage.setItem("savedPath", "/index/dashboard/");
        this.$refs.toast.showToast("success", "Login successfully!");
        setTimeout(() => {
          this.$router.push(`/index/dashboard/`);
          this.$router.go(0);
        }, 2000);
      } else {
        // Swal.fire({
        //   title: "Error!",
        //   text: "Invalid login credentials",
        //   icon: "error",
        // });
        this.$refs.toast.showToast("danger", "Invalid login credentials!");
      }
    },
  },
};
</script>
<style></style>
