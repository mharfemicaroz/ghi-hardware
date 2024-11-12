<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Voucher List</h4>
      <h6>Manage your Voucher</h6>
    </div>
    <div class="page-btn">
      <router-link
        class="btn btn-added"
        @click="navigateTo('/index/addvoucher')"
        to="/index/addvoucher"
      >
        <img src="/img/icons/plus.svg" class="me-1" alt="img" />Add Voucher
      </router-link>
    </div>
  </div>
  <TableComponent
    :mainHeaders="headers"
    :mainItems="filteredVoucher"
    :editable="true"
    @edit-action="editAction"
  />
  <ToasterComponent ref="toast" />
  <div
    class="modal fade show"
    id="editModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="editModalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="editModalLabel">Edit Voucher</h4>
          <button
            type="button"
            class="close"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-4 col-sm-6 col-12">
              <div class="form-group">
                <label>Name</label>
                <input type="text" v-model="voucher.name" />
              </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12">
              <div class="form-group">
                <label>Mode</label>
                <select
                  class="form-control"
                  @change="toggleSelect"
                  v-model="voucher.mode"
                  required
                >
                  <option value="0">Percentage-Based Discount</option>
                  <option value="1">Fixed Amount Discount</option>
                  <option value="2">Special Offer Price</option>
                </select>
              </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12">
              <div class="form-group">
                <label>{{
                  voucher.mode == 0
                    ? "Percentage"
                    : voucher.mode == 1
                    ? "Fixed Amount"
                    : "Special Price"
                }}</label>
                <input
                  v-if="voucher.mode == 0"
                  type="number"
                  class="form-control"
                  min="0"
                  step="0.01"
                  max="100"
                  v-model="voucher.discountPercentage"
                  required
                />
                <input
                  v-else-if="voucher.mode == 1"
                  type="number"
                  class="form-control"
                  min="0"
                  step="0.01"
                  v-model="voucher.discount"
                  required
                />
                <input
                  v-else-if="voucher.mode == 2"
                  type="number"
                  class="form-control"
                  min="0"
                  step="0.01"
                  v-model="voucher.specialPrice"
                  required
                />
              </div>
            </div>
            <div class="col-lg-6 col-sm-6 col-12">
              <div class="form-group">
                <label>Start Date </label>
                <div class="input-groupicon">
                  <input
                    type="date"
                    class="form-control"
                    v-model="voucher.startDate"
                    required
                  />
                </div>
              </div>
            </div>
            <div class="col-lg-6 col-sm-6 col-12">
              <div class="form-group">
                <label>Expiration Date </label>
                <div class="input-groupicon">
                  <input
                    type="date"
                    class="form-control"
                    v-model="voucher.expirationDate"
                    required
                  />
                </div>
              </div>
            </div>
            <div class="col-lg-12">
              <div class="form-group">
                <label>Description</label>
                <textarea
                  class="form-control"
                  v-model="voucher.desc"
                ></textarea>
              </div>
            </div>
            <div class="col-lg-12">
              <a
                href="javascript:void(0);"
                @click="saveAction"
                class="btn btn-submit me-2"
                >Submit</a
              >
              <a
                href="javascript:void(0);"
                class="btn btn-cancel"
                data-bs-dismiss="modal"
                aria-label="Close"
              >
                Cancel
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import ToasterComponent from "../../common/ToasterComponent.vue";
import TableComponent from "../../common/TableComponent.vue";
import { productVoucherApi } from "@/services/productServices";
export default {
  components: {
    ToasterComponent,
    TableComponent,
  },
  data() {
    return {
      currentId: null,
      voucher: {
        name: "",
        desc: "",
        mode: "0",
        discountPercentage: 0,
        discount: 0,
        specialPrice: 0,
        startDate: "",
        expirationDate: "",
      },
      headers: [
        {
          label: "Voucher Name",
          field: "name",
        },
        {
          label: "Description",
          field: "desc",
        },
        {
          label: "Code",
          field: "code",
        },
        {
          label: "Start Date",
          field: "startDate",
        },
        {
          label: "Expiration Date",
          field: "expirationDate",
        },
        {
          label: "",
          field: "action",
          sortable: false,
        },
      ],
      vouchers: [],
    };
  },
  computed: {
    filteredVoucher() {
      return this.vouchers.map((o) => {
        let code = "";

        if (o.discountPercentage == 0 && o.discount == 0) {
          code = `Special Price Offer: ${parseFloat(o.specialPrice)}`;
        } else if (o.discountPercentage != 0 && o.specialPrice == 0) {
          code = `Flexi - ${parseFloat(o.discountPercentage)}% off`;
        } else if (o.discount != 0 && o.discountPercentage == 0) {
          code = `Fix - ${o.discount} off`;
        } else {
          // Handle other cases here if needed
          code = "Other Case";
        }
        return {
          ...o,
          code: code,
        };
      });
    },
  },
  methods: {
    navigateTo(path, propSidebar = true) {
      // Adding a unique timestamp as a query parameter to force reload

      // Saving path to localStorage
      const isSidebar = propSidebar || true;
      localStorage.setItem("savedPath", path);
      localStorage.setItem("propSidebar", isSidebar);
      this.$router.push(path);
    },
    async loadData() {
      const response = await productVoucherApi.fetchAll();
      this.vouchers = response;
    },
    async editAction(id) {
      jQuery("#editModal").modal("toggle");
      this.currentId = id;
      const response = await productVoucherApi.fetchOne(id);
      this.voucher = {
        name: response.name,
        desc: response.desc,
        expirationDate: response.expirationDate
          .toString()
          .replace("T00:00:00Z", ""),
        discountPercentage: response.discountPercentage,
        startDate: response.startDate.toString().replace("T00:00:00Z", ""),
        discountPercentage: response.discountPercentage,
        discount: response.discount,
        specialPrice: response.specialPrice,
        mode: response.mode,
      };
    },
    async saveAction(id) {
      if (
        new Date(this.voucher.expirationDate) < new Date(this.voucher.startDate)
      ) {
        this.$refs.toast.showToast(
          "danger",
          "Expiration date must not be before the start date."
        );
        this.voucher.expirationDate = "";
        return false;
      }
      jQuery("#editModal").modal("toggle");
      await productVoucherApi.edit(this.currentId, this.voucher);
      this.loadData();
    },
  },
  async created() {
    this.loadData();
  },
};
</script>
<style></style>
