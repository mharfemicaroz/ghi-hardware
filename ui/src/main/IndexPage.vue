<template>
  <GlobalLoader v-if="isLoading" />
  <div class="main-wrapper">
    <HeaderComponent />
    <SideBar />
    <div class="page-wrapper">
      <div class="content">
        <router-view :key="$route.path"></router-view>
      </div>
    </div>
  </div>
</template>
<script>
import GlobalLoader from "../common/GlobalLoader.vue";
import HeaderComponent from "../common/HeaderComponent.vue";
import SideBar from "../common/SideBar.vue";

export default {
  components: {
    GlobalLoader,
    HeaderComponent,
    SideBar,
  },
  data() {
    return {
      isLoading: true, // Initially set to true to show loading state
    };
  },
  watch: {
    // Watch for route changes
    $route: {
      immediate: true, // Run the handler immediately
      handler() {
        // Use nextTick to wait until the next DOM update cycle
        this.$nextTick(() => {
          this.isLoading = true;

          // Set a timeout of 1000 milliseconds (1 second)
          setTimeout(() => {
            this.isLoading = false;
          }, 1000);
        });
      },
    },
  },
  created() { },
  mounted() {
    this.$router.push({ path: localStorage.getItem("savedPath") });

  },
};
</script>
<style></style>
