<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Purchase Add</h4>
      <h6>Add/Update Purchase</h6>
    </div>
  </div>
  <div class="card">
    <div class="card-body">
      <form @submit.prevent="addPurchase">
        <div class="row">
          <div class="col-lg-3 col-sm-6 col-12">
            <div class="form-group">
              <label>Supplier Name</label>
              <div class="row">
                <div class="col-lg-10 col-sm-10 col-10">
                  <select class="form-select" v-model="supplier" required>
                    <option
                      v-for="(item, index) in suppliers"
                      :key="index"
                      :value="item.id"
                    >
                      {{ item.name }}
                    </option>
                  </select>
                </div>
                <div class="col-lg-2 col-sm-2 col-2 ps-0">
                  <div class="add-icon">
                    <a href="javascript:void(0);"
                      ><img src="/img/icons/plus1.svg" alt="img"
                    /></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-sm-6 col-12">
            <div class="form-group">
              <label>Purchase Date </label>
              <div class="input-groupicon">
                <input
                  type="date"
                  class="form-control"
                  v-model="purchaseDate"
                  required
                />
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-sm-6 col-12">
            <div class="form-group">
              <label>Reference No.</label>
              <input type="text" v-model="refno" required />
            </div>
          </div>
          <div class="col-lg-3 col-sm-6 col-12">
            <div class="form-group">
              <label>Progress Status</label>
              <select class="form-select" v-model="progressStatus" required>
                <option value="">Choose</option>
                <option value="Ordered">Ordered</option>
                <option value="Pending">Pending</option>
                <option value="Received">Received</option>
              </select>
            </div>
          </div>
          <div class="col-lg-12 col-sm-6 col-12">
            <div class="form-group">
              <label>Product Name</label>
              <div class="input-groupicon">
                <form @submit.prevent="viewItem" autocomplete="off">
                  <input
                    type="text"
                    id="productItems"
                    placeholder="Search Product by code and select to add..."
                  />
                  <div class="addonset">
                    <img src="/img/icons/scanners.svg" alt="img" />
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="table-responsive">
            <table class="table">
              <thead>
                <tr>
                  <th>Product Name</th>
                  <th>QTY</th>
                  <th>Purchase Price(₱)</th>
                  <th>Discount %</th>
                  <th>Discount Amount(₱)</th>
                  <th>Tax %</th>
                  <th>Tax Amount(₱)</th>
                  <th class="text-end">Total Cost (₱)</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item of filteredPurchaseBook">
                  <td>
                    <a href="javascript:void(0);">{{ item.name }}</a>
                  </td>
                  <td>{{ item.qty }}</td>
                  <td>{{ item.price }}</td>
                  <td>{{ item.discountPercent }}</td>
                  <td>{{ item.discount }}</td>
                  <td>{{ item.taxPercent }}</td>
                  <td>{{ item.tax }}</td>
                  <td class="text-end">{{ item.totalCost }}</td>
                  <td>
                    <a @click="deleteItem(item.name)"
                      ><img src="/img/icons/delete.svg" alt="svg"
                    /></a>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-12 float-md-right">
            <div class="total-order">
              <ul>
                <li>
                  <h4>Order Tax</h4>
                  <h5>₱ {{ taxCost }}</h5>
                </li>
                <li>
                  <h4>Discount</h4>
                  <h5>₱ {{ discountCost }}</h5>
                </li>
                <li>
                  <h4>Shipping</h4>
                  <h5>₱ {{ shippingCost.toFixed(2) }}</h5>
                </li>
                <li class="total">
                  <h4>Grand Total</h4>
                  <h5>₱ {{ grandTotal }}</h5>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-3 col-sm-6 col-12">
            <div class="form-group">
              <label>Order Tax</label>
              <input
                type="number"
                min="0"
                max="100"
                step="0.01"
                class="form-control"
                v-model="taxPercent"
                required
              />
            </div>
          </div>
          <div class="col-lg-3 col-sm-6 col-12">
            <div class="form-group">
              <label>Discount</label>
              <input
                type="number"
                min="0"
                max="100"
                step="0.01"
                class="form-control"
                v-model="discountPercent"
                required
              />
            </div>
          </div>
          <div class="col-lg-3 col-sm-6 col-12">
            <div class="form-group">
              <label>Shipping</label>
              <input
                type="number"
                class="form-control"
                min="0"
                step="0.01"
                v-model="shippingCost"
                required
              />
            </div>
          </div>
          <div class="col-lg-3 col-sm-6 col-12">
            <div class="form-group">
              <label>Payment Status</label>
              <select class="form-select" v-model="paidStatus" required>
                <option value="">Choose</option>
                <option value="Unpaid">Unpaid</option>
                <option value="Partial">Partial</option>
                <option value="Paid">Paid</option>
              </select>
            </div>
          </div>
          <div class="col-lg-12">
            <div class="form-group">
              <label>Description</label>
              <textarea class="form-control" v-model="desc"></textarea>
            </div>
          </div>
          <div class="col-lg-12">
            <button type="submit" class="btn btn-submit me-2">Submit</button>
            <router-link
              class="btn btn-cancel"
              @click="navigateTo('/index/purchaselist')"
              to="/index/purchaselist"
            >
              Cancel
            </router-link>
          </div>
        </div>
      </form>
    </div>
  </div>
  <div
    class="modal fade show"
    id="itemModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="itemModalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="itemModalLabel">Load Product</h4>
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
            <div class="col-lg-6 col-sm-6 col-12">
              <div class="form-group">
                <label>Product Name</label>
                <input type="text" v-model="product.name" readonly />
              </div>
            </div>
            <div class="col-lg-3 col-sm-6 col-12">
              <div class="form-group">
                <label>Qty</label>
                <input
                  type="number"
                  min="0"
                  step="1"
                  v-model="product.qty"
                  class="form-control"
                />
              </div>
            </div>
            <div class="col-lg-3 col-sm-6 col-12">
              <div class="form-group">
                <label>Purchase Price (₱)</label>
                <input
                  type="number"
                  min="0"
                  step="0.01"
                  v-model="product.price"
                  class="form-control"
                />
              </div>
            </div>
            <div class="col-lg-3 col-sm-6 col-12">
              <div class="form-group">
                <label>Discount %</label>
                <input
                  type="number"
                  min="0"
                  max="100"
                  step="0.01"
                  @change="product.discount = 0"
                  @input="product.discount = 0"
                  v-model="product.discountPercent"
                  class="form-control"
                />
              </div>
            </div>
            <div class="col-lg-3 col-sm-6 col-12">
              <div class="form-group">
                <label>Discount Amount (₱)</label>
                <input
                  type="number"
                  min="0"
                  step="0.01"
                  @change="product.discountPercent = 0"
                  @input="product.discountPercent = 0"
                  v-model="product.discount"
                  class="form-control"
                />
              </div>
            </div>
            <div class="col-lg-3 col-sm-6 col-12">
              <div class="form-group">
                <label>Tax %</label>
                <input
                  type="number"
                  min="0"
                  max="100"
                  step="0.01"
                  @change="product.tax = 0"
                  @input="product.tax = 0"
                  v-model="product.taxPercent"
                  class="form-control"
                />
              </div>
            </div>
            <div class="col-lg-3 col-sm-6 col-12">
              <div class="form-group">
                <label>Tax Amount (₱)</label>
                <input
                  type="number"
                  min="0"
                  step="0.01"
                  @change="product.taxPercent = 0"
                  @input="product.taxPercent = 0"
                  v-model="product.tax"
                  class="form-control"
                />
              </div>
            </div>
            <div class="col-lg-12">
              <a
                href="javascript:void(0);"
                @click="insertItem"
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
  <ToasterComponent ref="toast" />
</template>
<script>
import ToasterComponent from "../../common/ToasterComponent.vue";
import { purchaseOrderApi, purchaseItemApi } from "@/services/purchaseServices";
import { peopleSupplierApi } from "@/services/PeopleServices";
import { productItemApi } from "@/services/ProductServices";
export default {
  components: {
    ToasterComponent,
  },
  data() {
    return {
      product: {
        name: "",
        qty: 0,
        price: 0,
        discount: 0,
        discountPercent: 0,
        tax: 0,
        taxPercent: 0,
      },
      supplier: "",
      purchaseDate: "",
      refno: "",
      progressStatus: "",
      paidStatus: "",
      taxPercent: 0,
      discountPercent: 0,
      shippingCost: 0,
      products: [],
      suppliers: [],
      purchaseBook: [],
    };
  },
  computed: {
    subtotal() {
      return this.filteredPurchaseBook.reduce(
        (acc, item) => acc + parseFloat(item.totalCost),
        0
      );
    },
    taxCost() {
      return (this.subtotal * (this.taxPercent / 100)).toFixed(2);
    },
    discountCost() {
      return (this.subtotal * (this.discountPercent / 100)).toFixed(2);
    },
    grandTotal() {
      return (
        this.subtotal +
        parseFloat(this.taxCost) -
        parseFloat(this.discountCost) +
        parseFloat(this.shippingCost)
      ).toFixed(2);
    },
    filteredPurchaseBook() {
      return this.purchaseBook;
    },
  },
  methods: {
    async loaddata() {
      this.suppliers = await peopleSupplierApi.fetchAll();
      this.products = await productItemApi.fetchAll();
      this.autocomplete(
        document.getElementById("productItems"),
        this.products.map((item) => item.name)
      );
    },
    resetValues() {},
    async addPurchase() {
      await purchaseOrderApi
        .filter({
          columnName: "refno",
          columnKey: this.refno,
        })
        .then(async (result) => {
          if (result.length > 0) {
            this.$refs.toast.showToast(
              "danger",
              "Purchase order with this reference no. already exists."
            );
            this.refno = "";
          } else {
            try {
              await purchaseOrderApi
                .add({
                  supplier: this.supplier,
                  purchaseDate: this.purchaseDate,
                  refno: this.refno,
                  progressStatus: this.progressStatus,
                  paidStatus: this.paidStatus,
                  taxPercent: this.taxPercent,
                  discountPercent: this.discountPercent,
                  shippingCost: this.shippingCost,
                  desc: this.desc,
                  lastCost: this.grandTotal,
                  lastBalance: this.grandTotal,
                  totalPaid: 0,
                })
                .then(async (response) => {
                  for (const item of this.purchaseBook) {
                    await purchaseItemApi.add({
                      product: item.id,
                      purchaseOrder: response.id,
                      price: item.price,
                      qty: item.qty,
                      discountPercent: item.discountPercent,
                      discount: item.discount,
                      taxPercent: item.taxPercent,
                      tax: item.tax,
                      totalCost: item.totalCost,
                    });
                  }
                });

              localStorage.setItem("savedPath", "/index/purchaselist/");
              this.$router.push(`/index/purchaselist/`);
            } catch (error) {
              console.error(error);
            }
          }
        });
    },
    navigateTo(path, propSidebar = true) {
      const isSidebar = propSidebar || true;
      localStorage.setItem("savedPath", path);
      localStorage.setItem("propSidebar", isSidebar);
      this.$router.push(path);
    },
    deleteItem(name) {
      const index = this.purchaseBook.findIndex((item) => item.name === name);
      if (index !== -1) {
        this.purchaseBook.splice(index, 1);
      }
    },
    viewItem() {
      const query = document.getElementById("productItems").value;
      const isExist =
        this.products.filter((o) =>
          o.name.toLowerCase().includes(query.toLowerCase())
        ).length === 0;
      const isLoaded =
        this.purchaseBook.filter((o) =>
          o.name.toLowerCase().includes(query.toLowerCase())
        ).length === 0;
      if (!isExist && !isLoaded) {
        document.getElementById("productItems").value = "";
        return false;
      }
      this.product = {
        name: query,
        qty: 0,
        price: 0,
        discount: 0,
        discountPercent: 0,
        tax: 0,
        taxPercent: 0,
      };
      jQuery("#itemModal").modal("toggle");
      document.getElementById("productItems").value = "";
    },
    insertItem() {
      jQuery("#itemModal").modal("toggle");
      const totalCost =
        parseFloat(this.product.qty) * parseFloat(this.product.price);
      const discountedTotalCost =
        this.product.discount === 0
          ? totalCost * (1 - this.product.discountPercent / 100)
          : totalCost - this.product.discount;
      const taxedTotalCost =
        this.product.tax === 0
          ? discountedTotalCost * (1 + this.product.taxPercent / 100)
          : discountedTotalCost - this.product.tax;
      const newCost = taxedTotalCost.toFixed(2);
      const productId = this.products.filter(
        (o) => o.name === this.product.name
      )[0].id;
      const arr = { ...this.product, totalCost: newCost, id: productId };
      this.purchaseBook.push(arr);
      document.getElementById("productItems").value = "";
    },
    autocomplete(inputField, autoCompleteArray) {
      let currentFocus;
      const vm = this;
      const maxItems = 10; // Maximum number of autocomplete items to display

      const closeAllLists = (element) => {
        const lists = document.querySelectorAll(".autocomplete-items");
        lists.forEach((list) => {
          if (element !== list && element !== inputField) {
            list.parentNode.removeChild(list);
          }
        });
      };

      inputField?.addEventListener("input", function () {
        const value = this.value;
        closeAllLists();
        if (!value) return;

        currentFocus = -1;
        const autoCompleteDiv = document.createElement("div");
        autoCompleteDiv.id = inputField.id + "autocomplete-list";
        autoCompleteDiv.className = "autocomplete-items";
        inputField.parentNode.appendChild(autoCompleteDiv);

        let itemCount = 0; // Counter for the number of displayed items
        autoCompleteArray.forEach((item) => {
          if (
            item.toUpperCase().startsWith(value.toUpperCase()) &&
            itemCount < maxItems
          ) {
            const autoCompleteItem = document.createElement("div");
            autoCompleteItem.innerHTML = `<strong>${item.substr(
              0,
              value.length
            )}</strong>${item.substr(value.length)}`;
            autoCompleteItem.innerHTML += `<input type='hidden' value='${item}'>`;
            autoCompleteItem?.addEventListener("click", function () {
              inputField.value = this.getElementsByTagName("input")[0].value;
              vm.viewItem();
              closeAllLists();
            });
            autoCompleteDiv.appendChild(autoCompleteItem);
            itemCount++;
          }
        });
      });

      inputField?.addEventListener("keydown", function (e) {
        const autoCompleteItems = document
          .getElementById(inputField.id + "autocomplete-list")
          ?.querySelectorAll("div");
        if (!autoCompleteItems) return;

        if (e.keyCode === 40) {
          currentFocus++;
          if (currentFocus >= autoCompleteItems.length) currentFocus = 0;
        } else if (e.keyCode === 38) {
          currentFocus--;
          if (currentFocus < 0) currentFocus = autoCompleteItems.length - 1;
        } else if (e.keyCode === 13) {
          e.preventDefault();
          if (currentFocus > -1) {
            autoCompleteItems[currentFocus].click();
          }
        }

        autoCompleteItems.forEach((item, index) => {
          if (index === currentFocus) {
            item.classList.add("autocomplete-active");
          } else {
            item.classList.remove("autocomplete-active");
          }
        });
      });

      document.addEventListener("click", function (e) {
        closeAllLists(e.target);
      });
    },
  },
  mounted() {
    this.loaddata();
  },
};
</script>
<style>
.autocomplete {
  /*the container must be positioned relative:*/
  position: relative;
  display: inline-block;
}
.autocomplete-items {
  position: absolute;
  border: 1px solid #d4d4d4;
  border-bottom: none;
  border-top: none;
  z-index: 99;
  /*position the autocomplete items to be the same width as the container:*/
  top: 100%;
  left: 0;
  right: 0;
}
.autocomplete-items div {
  padding: 10px;
  cursor: pointer;
  background-color: #fff;
  border-bottom: 1px solid #d4d4d4;
}
.autocomplete-items div:hover {
  /*when hovering an item:*/
  background-color: #e9e9e9;
}
.autocomplete-active {
  /*when navigating through the items using the arrow keys:*/
  background-color: DodgerBlue !important;
  color: #ffffff;
}
</style>
