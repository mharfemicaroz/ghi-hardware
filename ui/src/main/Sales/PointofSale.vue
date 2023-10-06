<template>
  <GlobalLoader />
  <div class="main-wrappers">
    <HeaderComponent />
    <div class="page-wrapper ms-0">
      <div class="content">
        <div class="row">
          <div class="col-lg-8 col-sm-12 tabs_wrapper">
            <div class="row">
              <div class="col-lg-12 p-0">
                <div class="card mb-2">
                  <div class="card-body">
                    <form @submit.prevent="insertItem">
                      <div class="input-group">
                        <span class="input-group-text text-white btn-primary"
                          ><i class="fa fa-search"></i
                        ></span>

                        <input
                          id="productItems"
                          ref="productItems"
                          type="text"
                          class="form-control"
                          placeholder="Enter item name or scan barcode"
                          aria-label="Search"
                          autocomplete="off"
                          aria-autocomplete="off"
                        />

                        <span class="input-group-text text-white btn-primary"
                          ><i class="fa fa-table m"></i> &nbsp;Show Grid</span
                        >
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-lg-12 p-0">
                <div class="card">
                  <div class="card-body">
                    <div
                      class="table-responsive"
                      style="
                        height: fit-content;
                        max-height: 600px;
                        overflow-y: auto;
                        overflow-x: hidden;
                      "
                    >
                      <table class="table">
                        <thead>
                          <tr>
                            <th style="width: 500px; text-align: center">
                              Item Name
                            </th>
                            <th style="text-align: center">Price</th>
                            <th style="text-align: center">Qty.</th>
                            <th style="text-align: center">Disc %</th>
                            <th class="text-center">Total</th>
                            <th class="text-center"></th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr v-for="(item, index) of salesBook">
                            <td>
                              <a href="javascript:void(0);">{{ item.name }}</a>
                            </td>
                            <td class="text-center">{{ item.price }}</td>
                            <td
                              style="
                                width: 100px;
                                text-align: center;
                                margin: auto;
                              "
                            >
                              <span v-if="!itemStatus[index]">{{
                                item.qty
                              }}</span>
                              <input
                                v-else
                                class="form-control"
                                type="number"
                                min="1"
                                step="1"
                                v-model="book.qty[index]"
                              />
                            </td>
                            <td
                              style="
                                width: 100px;
                                text-align: center;
                                margin: auto;
                              "
                            >
                              <span v-if="!itemStatus[index]">{{
                                item.discountPercent
                              }}</span>
                              <input
                                v-else
                                class="form-control"
                                type="number"
                                min="0"
                                max="100"
                                step="0.01"
                                v-model="book.discountPercent[index]"
                              />
                            </td>
                            <td
                              style="
                                width: 120px;
                                text-align: center;
                                margin: auto;
                              "
                            >
                              <span v-if="!itemStatus[index]">{{
                                item.totalCost
                              }}</span>
                              <input
                                v-else
                                class="form-control"
                                type="text"
                                readonly
                                :value="calculateNewCost(index)"
                              />
                            </td>
                            <td class="text-center" style="font-size: medium">
                              <span v-if="!itemStatus[index]">
                                <a
                                  class="me-3 dropset"
                                  data-bs-toggle="dropdown"
                                  aria-expanded="false"
                                  href="javascript:void(0);"
                                  ><img
                                    src="/img/icons/ellipise1.svg"
                                    alt="img"
                                /></a>
                                <ul
                                  class="dropdown-menu"
                                  aria-labelledby="dropdownMenuButton"
                                  data-popper-placement="bottom-end"
                                >
                                  <li>
                                    <a
                                      href="javascript:void(0);"
                                      class="dropdown-item"
                                      @click="editItem(index)"
                                      >Edit</a
                                    >
                                  </li>
                                  <li>
                                    <a
                                      href="javascript:void(0);"
                                      class="dropdown-item"
                                      @click="deleteItem(index)"
                                      >Delete</a
                                    >
                                  </li>
                                </ul>
                              </span>
                              <span v-else>
                                <a
                                  style="font-size: medium"
                                  class="btn btn-small btn-primary"
                                  href="javascript:void(0);"
                                  @click="
                                    saveItem(item.id, index, item.product)
                                  "
                                  ><i class="fa fa-save text-white"></i
                                ></a>
                              </span>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                      <div class="row mt-3" v-if="salesBook.length === 0">
                        <div class="col-lg-12 text-center">
                          <h3 class="text-muted">
                            There are no items in the cart.
                          </h3>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-sm-12">
            <div class="row">
              <div class="col-lg-12">
                <div class="card mb-0">
                  <div class="card-body text-center">
                    <span>
                      <button type="button" class="btn btn-light">
                        <i class="fa fa-question"></i>
                      </button>
                    </span>
                    <span v-if="salesBook.length > 0">
                      <!-- &nbsp;
                      <button type="button" class="btn btn-primary">
                        <i class="fa fa-pause"></i>&nbsp;Suspend Sales
                      </button> -->
                      &nbsp;
                      <button
                        type="button"
                        class="btn btn-primary"
                        @click="cancelSales"
                      >
                        <i class="fa fa-times-circle"></i>&nbsp;Cancel Sales
                      </button>
                    </span>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-lg-12">
                <div class="card mt-2 mb-0">
                  <div class="card-body">
                    <div class="input-group">
                      <span class="input-group-text text-white btn-primary"
                        ><i class="fa fa-user-plus"></i
                      ></span>
                      <input
                        type="text"
                        id="customerItems"
                        v-model="customer"
                        class="form-control"
                        placeholder="Type customer name..."
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-lg-12">
                <div class="card mt-2 mb-0">
                  <div class="card-body">
                    <div class="row mb-3">
                      <div class="col-lg-8">
                        <p>Discount all Items by Percent:</p>
                      </div>
                      <div class="col-lg-4 text-end">
                        <a
                          v-if="!isClickDiscOne"
                          href="javascript:void(0);"
                          @click="
                            salesBook.length > 0 ? (isClickDiscOne = true) : ''
                          "
                          >{{ itemDiscount.toFixed(2) }}%</a
                        >
                        <span v-else class="input-group">
                          <input
                            type="number"
                            min="0"
                            max="100"
                            step="0.01"
                            class="form-control"
                            v-model="itemDiscount"
                          />
                          &nbsp;
                          <a
                            class="input-group-text"
                            href="javascript:void(0);"
                            @click="setAllItemsDiscount"
                            ><i class="fa fa-check"></i
                          ></a>
                        </span>
                      </div>
                    </div>

                    <div class="row mb-3">
                      <div class="col-lg-8">
                        <p>Discount Entire Sale:</p>
                      </div>
                      <div class="col-lg-4 text-end">
                        <a
                          v-if="!isClickDiscAll"
                          href="javascript:void(0);"
                          @click="isClickDiscAll = true"
                          >{{ discountPercent.toFixed(2) }}%</a
                        >
                        <span v-else class="input-group">
                          <input
                            type="number"
                            min="0"
                            max="100"
                            step="0.01"
                            class="form-control"
                            v-model="discountPercent"
                          />
                          &nbsp;
                          <a
                            class="input-group-text"
                            href="javascript:void(0);"
                            @click="isClickDiscAll = false"
                            ><i class="fa fa-check"></i
                          ></a>
                        </span>
                      </div>
                    </div>

                    <div class="row mb-3">
                      <div class="col-lg-8 font-weight-bold">
                        <p>Sub Total:</p>
                      </div>
                      <div class="col-lg-4 text-end font-weight-bold">
                        ₱ {{ subtotal.toFixed(2) }}
                      </div>
                    </div>

                    <div class="row mb-3">
                      <div class="col-lg-8">
                        <p>
                          <a
                            v-if="!isClickTax"
                            href="javascript:void(0);"
                            @click="isClickTax = true"
                            >{{ taxPercent.toFixed(2) }} % Tax</a
                          >
                          <span v-else class="input-group" style="width: 200px">
                            <input
                              type="number"
                              min="0"
                              max="100"
                              step="0.01"
                              class="form-control"
                              v-model="taxPercent"
                            />
                            &nbsp;
                            <a
                              class="input-group-text"
                              href="javascript:void(0);"
                              @click="isClickTax = false"
                              ><i class="fa fa-check"></i
                            ></a>
                            &nbsp % Tax
                          </span>
                        </p>
                      </div>
                      <div class="col-lg-4 text-end">
                        ₱ {{ ((subtotal * taxPercent) / 100).toFixed(2) }}
                      </div>
                    </div>

                    <div class="row mb-0 dashed-border">
                      <div class="col">
                        <h4>Total</h4>
                      </div>
                      <div class="col">
                        <h4>Change</h4>
                      </div>
                    </div>

                    <div class="row mt-0 mb-3">
                      <div class="col text-center text-success dashed-border">
                        <h3 class="fw-bold">₱ {{ netTotal }}</h3>
                      </div>
                      <div class="col text-center bg-lightyellow dashed-border">
                        <h3 class="fw-bold text-warning">₱ {{ change }}</h3>
                      </div>
                    </div>
                    <form @submit.prevent="payOrder">
                      <div class="input-group">
                        <select
                          class="form-control"
                          v-model="paymentMode"
                          required
                        >
                          <option value="cash">Cash</option>
                          <option value="GCash">GCash</option>
                          <option value="PayMaya">PayMaya</option>
                          <option value="Check">Check</option>
                          <option value="Credit Card">Credit Card</option>
                          <option value="Debit Card">Debit Card</option>
                        </select>
                        <div class="input-group-append">
                          <input
                            type="text"
                            class="form-control"
                            v-model="refno"
                            placeholder="Reference no."
                            required
                          />
                        </div>
                      </div>
                      <div class="input-group" style="height: 50px">
                        <input
                          type="number"
                          placeholder="Enter cash amount"
                          v-model="amountPaid"
                          min="0"
                          step="0.01"
                          class="form-control"
                          @keyup="updateTotalCash"
                          @keydown="updateTotalCash"
                          required
                        />
                        <div class="input-group-append">
                          <button
                            :disabled="
                              isClickDiscOne ||
                              isClickDiscAll ||
                              isClickTax ||
                              amountPaid === 0 ||
                              salesBook.length === 0 ||
                              amountPaid !== netTotal
                            "
                            class="btn btn-primary"
                            type="submit"
                            style="height: 50px !important"
                          >
                            Add Payment
                          </button>
                        </div>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-lg-12">
                <div class="card mt-2">
                  <div class="card-body">
                    <textarea
                      v-model="desc"
                      class="form-control"
                      placeholder="Comments"
                    ></textarea>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- Modals -->
</template>
<script>
import GlobalLoader from "../../common/GlobalLoader.vue";
import HeaderComponent from "../../common/HeaderComponent.vue";
import { peopleCustomerApi } from "@/services/PeopleServices";
import { productItemApi } from "@/services/ProductServices";
import {
  salesOrderApi,
  salesItemApi,
  salesTransactionApi,
} from "@/services/SalesServices";
export default {
  components: {
    GlobalLoader,
    HeaderComponent,
  },
  data() {
    return {
      customer: "Walk-in",
      paymentMode: "cash",
      refno: "",
      desc: "",
      book: {
        qty: [],
        price: [],
        discountPercent: [],
      },
      itemStatus: [],
      salesitems: [],
      products: [],
      salesBook: [],
      partialTotal: 0,
      taxPercent: 0,
      itemDiscount: 0,
      discountPercent: 0,
      amountPaid: 0,
      isClickDiscOne: false,
      isClickDiscAll: false,
      isClickTax: false,
    };
  },
  computed: {
    subtotal() {
      return this.salesBook.reduce(
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
    netTotal() {
      return (
        this.subtotal +
        parseFloat(this.taxCost) -
        parseFloat(this.discountCost)
      ).toFixed(2);
    },
    change() {
      return (
        parseFloat(this.netTotal) < parseFloat(this.amountPaid)
          ? parseFloat(this.amountPaid) - parseFloat(this.netTotal)
          : 0
      ).toFixed(2);
    },
    grandTotal() {
      return (
        this.subtotal +
        parseFloat(this.taxCost) -
        parseFloat(this.discountCost) -
        parseFloat(this.partialTotal)
      ).toFixed(2);
    },
  },
  methods: {
    async loaddata() {
      this.customers = await peopleCustomerApi.fetchAll();
      this.products = await productItemApi.fetchAll();
      this.autocomplete(
        document.getElementById("productItems"),
        this.products
          .filter(
            (o) =>
              parseFloat(o.price) > 0 &&
              !o.isRecentPurchased &&
              o.qty - 1 > o.minqty
          )
          .map((item) => item.name)
      );
      this.autocomplete(
        document.getElementById("customerItems"),
        this.customers.map((item) => item.name)
      );
    },
    generateUniqueId() {
      const alphanumericChars =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

      const generateRandomString = (length) => {
        let randomString = "";
        for (let i = 0; i < length; i++) {
          const randomIndex = Math.floor(
            Math.random() * alphanumericChars.length
          );
          randomString += alphanumericChars.charAt(randomIndex);
        }
        return randomString;
      };

      const randomString = generateRandomString(4);
      const numericDate = new Date().getTime();
      return `${randomString}-${numericDate}`;
    },
    async payOrder() {
      await salesOrderApi
        .filter({
          columnName: "refno",
          columnKey: "pos-" + this.refno,
        })
        .then(async (result) => {
          if (result.length > 0) {
            this.$refs.toast.showToast(
              "danger",
              "Sales order with this reference no. already exists."
            );
            this.refno = "";
          } else {
            try {
              const customer = (
                this.customers.find((o) => o.name === this.customer) || {
                  id: null,
                }
              ).id;
              await salesOrderApi
                .add({
                  customer: customer,
                  salesDate: new Date(),
                  refno: "pos-" + this.refno,
                  progressStatus: "Completed",
                  paidStatus: "Paid",
                  taxPercent: this.taxPercent,
                  discountPercent: this.discountPercent,
                  shippingCost: 0,
                  desc: this.desc,
                  lastCost: this.amountPaid,
                  lastBalance: 0,
                  totalPaid: this.amountPaid,
                })
                .then(async (response) => {
                  for (const item of this.salesBook) {
                    await salesItemApi.add({
                      product: item.id,
                      salesOrder: response.id,
                      price: item.price,
                      qty: item.qty,
                      discountPercent: item.discountPercent,
                      discount: 0,
                      taxPercent: 0,
                      tax: 0,
                      totalCost: item.totalCost,
                    });
                  }
                  await salesTransactionApi.add({
                    cost: this.amountPaid,
                    balance: 0,
                    amountPaid: this.amountPaid,
                    status: "full",
                    refno:
                      this.paymentMode +
                      "-" +
                      this.refno +
                      "-" +
                      this.generateUniqueId(),
                    desc: this.desc,
                    salesOrder: response.id,
                  });
                  this.loaddata();
                  this.$router.go(0);
                });
            } catch (error) {
              console.error(error);
            }
          }
        });
    },

    updateTotalCash() {
      if (
        this.amountPaid === 0 ||
        this.amountPaid.toString() === "" ||
        this.amountPaid === NaN
      ) {
        this.amountPaid = 0;
      } else {
        this.amountPaid = this.amountPaid.toString();
      }
      //alert(this.totalCash)
    },
    calculateNewCost(index) {
      const qty = parseFloat(this.book.qty[index]);
      const price = parseFloat(this.book.price[index]);
      const discountPercent = this.book.discountPercent[index] / 100;

      const totalCost = qty * price;
      const discountedTotalCost = totalCost * (1 - discountPercent);
      return discountedTotalCost.toFixed(2);
    },
    setAllItemsDiscount() {
      if (this.salesBook.length > 0) {
        this.isClickDiscOne = false;
        this.salesBook.forEach((obj) => {
          obj.discountPercent = this.itemDiscount;
          obj.totalCost = (
            parseFloat(obj.price) *
            parseFloat(obj.qty) *
            (1 + this.itemDiscount / 100)
          ).toFixed(2);
        });
        this.book.discountPercent.forEach((element, index, array) => {
          array[index] = this.itemDiscount;
        });
      }
    },
    async cancelSales() {
      const result = await this.$swal.fire({
        icon: "warning",
        title: "Are you sure you want to clear this sale? ",
        text: "All items will cleared.",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        showCancelButton: true,
      });

      if (result.isConfirmed) {
        this.salesBook = [];
        this.itemStatus = [];
        ["qty", "price", "discountPercent"].forEach((prop) => {
          this.book[prop] = [];
        });
      }
    },
    editItem(index) {
      this.itemStatus[index] = true;
    },
    insertItem() {
      const query = document.getElementById("productItems").value;
      const isExist =
        this.products.filter((o) =>
          o.name.toLowerCase().includes(query.toLowerCase())
        ).length === 0;
      const isLoaded =
        this.salesBook.filter((o) =>
          o.name.toLowerCase().includes(query.toLowerCase())
        ).length === 0;
      if (!isExist && !isLoaded) {
        document.getElementById("productItems").value = "";
        return false;
      }
      const matchingProduct = this.products.find((o) =>
        o.name.toLowerCase().includes(query.toLowerCase())
      );
      const productId = matchingProduct?.id;
      const productName = matchingProduct?.name;
      const productPrice = matchingProduct?.price;
      this.salesBook.unshift({
        id: productId,
        name: productName,
        price: productPrice,
        qty: 1,
        discountPercent: 0,
        totalCost: productPrice,
      });
      ["qty", "price", "discountPercent"].forEach((prop) => {
        const entry =
          prop === "price" ? parseFloat(productPrice) : prop === "qty" ? 1 : 0;
        this.book[prop].unshift(entry);
      });
      this.itemStatus.unshift(false);
      document.getElementById("productItems").value = "";
      document.getElementById("productItems").focus();
    },
    async deleteItem(id, index) {
      this.salesBook.splice(index, 1);
      this.itemStatus.splice(index, 1);
      ["qty", "price", "discountPercent"].forEach((prop) => {
        this.book[prop].splice(index, 1);
      });
    },
    async saveItem(id, index) {
      this.itemStatus[index] = false;
      const getValue = (property) => this.book?.[property]?.[index] ?? 0;

      const newitem = this.salesBook.find((o) => o.id === id) || {};
      const properties = ["qty", "discountPercent"];

      properties.forEach((prop) => (newitem[prop] = getValue(prop)));
      newitem.totalCost = this.calculateNewCost(index);
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

      inputField.addEventListener("input", function () {
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
            autoCompleteItem.addEventListener("click", function () {
              inputField.value = this.getElementsByTagName("input")[0].value;
              // vm.insertItem();
              closeAllLists();
            });
            autoCompleteDiv.appendChild(autoCompleteItem);
            itemCount++;
          }
        });
      });

      inputField.addEventListener("keydown", function (e) {
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
    document.getElementById("productItems").focus();
  },
};
</script>
<style scoped>
.dashed-border {
  border: 0.1em dashed #ebebeb; /* 1px dashed border with black color */
}
</style>
