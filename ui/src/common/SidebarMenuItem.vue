<template>
  <li :class="{ submenu: hasSubmenu, subdrop: submenuOpen && hasSubmenu }">
    <a
      href="javascript:void(0);"
      :class="{ active: isActive }"
      @click="handleClick"
    >
      <span>{{ item.label }}</span>
      <span v-if="hasSubmenu" class="menu-arrow"></span>
    </a>
    <ul v-if="hasSubmenu" v-show="submenuOpen">
      <SidebarMenuItem
        v-for="(submenu, index) in item.submenu"
        :key="index"
        :item="submenu"
        @navigate="navigateTo"
        :route="route"
      />
    </ul>
  </li>
</template>

<script>
export default {
  name: "SidebarMenuItem",
  props: {
    item: {
      type: Object,
      required: true,
    },
    route: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      submenuOpen: false,
    };
  },
  computed: {
    hasSubmenu() {
      return Array.isArray(this.item.submenu);
    },
    isActive() {
      return this.route === this.item.route;
    },
  },
  methods: {
    handleClick() {
      if (this.hasSubmenu) {
        this.submenuOpen = !this.submenuOpen;
      } else {
        this.$emit("navigate", this.item);
      }
    },
    navigateTo(route) {
      this.$emit("navigate", route);
    },
  },
};
</script>
