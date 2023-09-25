<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Product Add Category</h4>
      <h6>Create new product Category</h6>
    </div>
  </div>

  <div class="card">
    <div class="card-body">
      <form @submit.prevent="addCategory">
        <div class="row">
          <div class="col-lg-6 col-sm-6 col-12">
            <div class="form-group">
              <label>Category Name</label>
              <input type="text" v-model="name" required />
            </div>
          </div>
          <div class="col-lg-6 col-sm-6 col-12">
            <div class="form-group">
              <label>Category Code</label>
              <input type="text" v-model="code" required />
            </div>
          </div>
          <div class="col-lg-12">
            <div class="form-group">
              <label>Description</label>
              <textarea class="form-control" v-model="desc"></textarea>
            </div>
          </div>
          <!-- <div class="col-lg-12">
            <div class="form-group">
              <label> {{ imageFileName }}</label>
              <div class="image-upload">
                <input type="file" id="image" @change="handleImageUpload" />
                <div class="image-uploads">
                  <img src="/img/icons/upload.svg" alt="img" />
                  <h4>Drag and drop a file to upload</h4>
                </div>
              </div>
            </div>
          </div> -->
          <div class="col-lg-12">
            <button type="submit" class="btn btn-submit me-2">Submit</button>
            <router-link
              class="btn btn-cancel"
              @click="navigateTo('/index/categorylist')"
              to="/index/categorylist"
            >
              Cancel
            </router-link>
          </div>
        </div>
      </form>
    </div>
  </div>
  <ToasterComponent ref="toast" />
</template>
<script>
import ToasterComponent from "../../common/ToasterComponent.vue";
import {
  productCategoryApi,
  saveImageProductCategory,
} from "@/services/productServices";

export default {
  components: {
    ToasterComponent,
  },
  data() {
    return {
      name: "",
      code: "",
      desc: "",
      // imageFile: null,
      // imageFileName: "",
    };
  },
  methods: {
    resetValues() {
      this.name = "";
      this.code = "";
      this.desc = "";
      // this.imageFile = null;
      // this.imageFileName = "";
    },
    async addCategory() {
      await productCategoryApi
        .filter({
          columnName: "name",
          columnKey: this.name,
        })
        .then(async (result) => {
          if (result.length > 0) {
            this.$refs.toast.showToast(
              "danger",
              "Product category with this name already exists."
            );
            this.resetValues();
          } else {
            await productCategoryApi
              .filter({
                columnName: "code",
                columnKey: this.code,
              })
              .then(async (result) => {
                if (result.length > 0) {
                  this.$refs.toast.showToast(
                    "danger",
                    "Product category with this code already exists."
                  );
                  this.resetValues();
                } else {
                  try {
                    const response = await productCategoryApi.add({
                      name: this.name,
                      code: this.code,
                      desc: this.desc,
                      author: this.author,
                      // image_filename: this.imageFileName,
                    });

                    // if (this.imageFileName !== "" && this.imageFile !== null) {
                    //   const formData = new FormData();
                    //   formData.append("file", this.imageFile, this.imageFileName);
                    //   await saveImageProductCategory(formData);
                    // }

                    localStorage.setItem("savedPath", "/index/categorylist/");
                    this.$router.push(`/index/categorylist/`);
                    setTimeout(() => {
                      this.$router.go(0);
                    }, 1);
                  } catch (error) {
                    console.error(error);
                  }
                }
              });
          }
        });
    },
    handleImageUpload(event) {
      const file = event.target.files[0];

      // Check if a file was selected
      if (!file) {
        // Handle error when no file is selected
        this.$refs.toast.showToast("danger", "No file selected.");
        return;
      }

      // Check if the file is an image
      if (!file.type.startsWith("image/")) {
        // Handle error when selected file is not an image
        this.$refs.toast.showToast("danger", "Selected file is not an image.");
        return;
      }

      // Check if the file size is within the limit (2MB)
      const maxSizeInBytes = 2 * 1024 * 1024; // 2MB
      if (file.size > maxSizeInBytes) {
        // Handle error when file size exceeds the limit

        this.$refs.toast.showToast(
          "danger",
          "Selected file exceeds the size limit (2MB)."
        );
        return;
      }

      // File passed all the validation checks, proceed with setting properties
      this.imageFile = file;

      const currentDate = new Date()
        .toISOString()
        .slice(0, 10)
        .replace(/-/g, "_");
      const uniqueID = Math.floor(100000 + Math.random() * 900000);
      const fileExtension = file.name.split(".").pop(); // Get the actual file extension
      const fileName = `productCategory_${currentDate}_${uniqueID}.${fileExtension}`;
      this.imageFileName = fileName;
    },
    navigateTo(path, propSidebar = true) {
      // Adding a unique timestamp as a query parameter to force reload

      // Saving path to localStorage
      const isSidebar = propSidebar || true;
      localStorage.setItem("savedPath", path);
      localStorage.setItem("propSidebar", isSidebar);
      this.$router.go(0);
    },
  },
};
</script>
<style></style>
