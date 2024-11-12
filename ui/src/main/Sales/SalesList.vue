<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Sales Management</h4>
      <h6>Manage your sales</h6>
    </div>
    <div class="page-btn">
      <router-link
        class="btn btn-added"
        @click="navigateTo('/index/salesadd')"
        to="/index/salesadd"
      >
        <img src="/img/icons/plus.svg" class="me-2" alt="img" />
        Add New Sales
      </router-link>
    </div>
  </div>
  <TableComponent
    :mainHeaders="headers"
    :mainItems="filteredsalesorders"
    :editable="false"
    :selectable="true"
    :batchAction="true"
    :moreAction="true"
    :actionBtns="['Edit Sales Order', 'Payments']"
    @btn-action1="editAction"
    @btn-action2="payAction"
  >
    <template #checkboxtrigger="data">
      <button class="btn btn-sm btn-primary">Update Status</button>
    </template>

    <template #content="data">
      <span
        v-if="data.data.h === 'progressStatus'"
        class="badges"
        :class="getBadgeClass(data.data.dt.progressStatus)"
      >
        {{ data.data.dt.progressStatus }}
      </span>

      <span
        v-else-if="data.data.h === 'paidStatus'"
        class="badges"
        :class="getBadgeClass(data.data.dt.paidStatus)"
      >
        {{ data.data.dt.paidStatus }}
      </span>
    </template>
  </TableComponent>
  <div
    class="modal fade show"
    id="payModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="payModalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="payModalLabel">Payment Module</h4>
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
            <div class="col-lg-8 col-sm-6 col-12">
              <div
                class="table-responsive"
                style="
                  height: fit-content;
                  max-height: 200px;
                  overflow-y: auto;
                  overflow-x: hidden;
                "
              >
                <table class="table">
                  <thead>
                    <tr>
                      <th>Cost</th>
                      <th>Amount Paid</th>
                      <th>Balance</th>
                      <th>Ref. #</th>
                      <th>Date</th>
                      <th>Status</th>
                      <th>Remarks</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item of filteredtransactionshistory">
                      <td>{{ item.cost }}</td>
                      <td>{{ item.amountPaid }}</td>
                      <td>{{ item.balance }}</td>
                      <td>{{ item.refno }}</td>
                      <td>{{ item.created }}</td>
                      <td>{{ item.status }}</td>
                      <td>{{ item.desc }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12">
              <div class="row">
                <div class="col-lg-12 float-md-right mb-0">
                  <div class="total-order mb-0 mt-0">
                    <ul>
                      <li class="total">
                        <h4>Subtotal</h4>
                        <h5>₱ {{ subtotal }}</h5>
                      </li>
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
                        <h5>₱ {{ salesorder.shippingCost }}</h5>
                      </li>
                      <li class="total">
                        <h4>Grand Total</h4>
                        <h5>₱ {{ netTotal }}</h5>
                      </li>
                      <li class="total">
                        <h4 class="text-danger">Partial Payment</h4>
                        <h5>
                          {{ partialTotal > 0 ? "-" : "" }}₱ {{ partialTotal }}
                        </h5>
                      </li>
                      <li class="total">
                        <h4>Total Balance</h4>
                        <h5>₱ {{ grandTotal }}</h5>
                      </li>
                    </ul>
                  </div>
                </div>
                <form id="payForm" @submit.prevent="payOrder">
                  <div class="form-group mb-1 mt-1">
                    <div class="input-group">
                      <span class="input-group-text">₱</span>
                      <input
                        type="number"
                        class="form-control"
                        v-model.number="salestransaction.amountPaid"
                        style="font-size: x-large; text-align: right"
                        step="0.01"
                        @keyup="updateTotalCash"
                        @keydown="updateTotalCash"
                        required
                      />
                      <span class="input-group-text">{{
                        (
                          salestransaction.amountPaid -
                          Math.floor(salestransaction.amountPaid)
                        )
                          .toFixed(2)
                          .substr(1)
                      }}</span>
                    </div>
                  </div>
                  <div class="col-md-12 mt-0">
                    <div class="row row-cols-1 row-cols-md-4">
                      <div
                        class="col mb-1"
                        v-for="item in cashDenominations"
                        :key="item.id"
                      >
                        <button
                          type="button"
                          class="btn bg-white rounded-lg shadow hover:shadow-xs focus:outline-none inline-block px-0 py-0 text-sm"
                          @click="addToCash(item.value)"
                        >
                          <span>{{ item.label }}</span>
                        </button>
                      </div>
                    </div>
                  </div>
                  <div class="form-group mb-0 mt-1">
                    <div class="input-group">
                      <span class="input-group-text">Reference #:</span>
                      <input
                        type="text"
                        class="form-control"
                        v-model="salestransaction.refno"
                        required
                      />
                    </div>
                  </div>
                  <div class="form-group mt-0">
                    <label>Description</label>
                    <textarea
                      class="form-control"
                      v-model="salestransaction.desc"
                      style="width: 100%; height: 100%; box-sizing: border-box"
                    ></textarea>
                  </div>
                  <div class="col-lg-12 mt-3">
                    <button type="submit" class="btn btn-submit me-2">
                      Pay
                    </button>
                    <a
                      href="javascript:void(0);"
                      class="btn btn-cancel"
                      data-bs-dismiss="modal"
                      aria-label="Close"
                    >
                      Cancel
                    </a>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade show"
    id="editModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="editModalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div
      class="modal-dialog"
      style="max-width: 1200px !important"
      role="document"
    >
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="editModalLabel">Edit Sales Order</h4>
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
          <form id="mainForm" @submit.prevent="saveAction">
            <div class="row">
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Customer Name</label>
                  <select
                    class="form-select"
                    v-model="salesorder.customer"
                    :disabled="isCompleted"
                  >
                    <option value="">Walk-in</option>
                    <option
                      v-for="(item, index) in customers"
                      :key="index"
                      :value="item.id"
                    >
                      {{ item.name }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Sales Date</label>
                  <input
                    type="date"
                    class="form-control"
                    v-model="salesorder.salesDate"
                    required
                    :disabled="isCompleted"
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Reference No.</label>
                  <input
                    type="text"
                    v-model="salesorder.refno"
                    required
                    :disabled="isCompleted"
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Progress Status</label>
                  <select
                    class="form-select"
                    v-model="salesorder.progressStatus"
                    required
                    :disabled="isCompleted"
                  >
                    <option value="">Choose</option>
                    <option value="On Progress">On Progress</option>
                    <option value="Pending">Pending</option>
                    <option value="Completed">Completed</option>
                  </select>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-lg-12 col-sm-6 col-12">
                <div class="form-group">
                  <label>Product Name</label>
                  <div class="input-groupicon">
                    <form @submit.prevent="insertItem" autocomplete="off">
                      <input
                        type="text"
                        id="productItems"
                        placeholder="Search Product by code and select to add..."
                        :disabled="salesorder.progressStatus === 'Completed'"
                      />
                      <div class="addonset">
                        <img src="/img/icons/scanners.svg" alt="img" />
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
            <div class="row mb-2" v-if="salesitems.length > 0">
              <div
                class="table-responsive"
                style="
                  height: fit-content;
                  max-height: 200px;
                  overflow-y: auto;
                  overflow-x: hidden;
                "
              >
                <table class="table">
                  <thead>
                    <tr>
                      <th>Product Name</th>
                      <th>QTY</th>
                      <th>Price(₱)</th>
                      <th>Discount %</th>
                      <th>Discount Amount(₱)</th>
                      <th>Tax %</th>
                      <th>Tax Amount(₱)</th>
                      <th class="text-end">Total Cost (₱)</th>
                      <th
                        v-if="!(salesorder.progressStatus === 'Received')"
                      ></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, index) of salesitems">
                      <td>
                        <a href="javascript:void(0);">{{ item.productName }}</a>
                      </td>
                      <td>
                        <span v-if="!itemStatus[index]">{{ item.qty }}</span>
                        <input
                          v-else
                          class="form-control"
                          type="number"
                          min="1"
                          :max="item.productMaxQty - 1"
                          step="1"
                          v-model="book.qty[index]"
                        />
                      </td>
                      <td>
                        <span v-if="!itemStatus[index]">{{ item.price }}</span>
                        <input
                          v-else
                          class="form-control"
                          type="number"
                          min="0"
                          step="1"
                          readonly
                          v-model="book.price[index]"
                        />
                      </td>
                      <td>
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
                          @input="book.discount[index] = 0"
                          @change="book.discount[index] = 0"
                        />
                      </td>
                      <td>
                        <span v-if="!itemStatus[index]">{{
                          item.discount
                        }}</span>
                        <input
                          v-else
                          class="form-control"
                          type="number"
                          min="0"
                          step="1"
                          v-model="book.discount[index]"
                          @input="book.discountPercent[index] = 0"
                          @change="book.discountPercent[index] = 0"
                        />
                      </td>
                      <td>
                        <span v-if="!itemStatus[index]">{{
                          item.taxPercent
                        }}</span>
                        <input
                          v-else
                          class="form-control"
                          type="number"
                          min="0"
                          max="100"
                          step="0.01"
                          v-model="book.taxPercent[index]"
                          @input="book.tax[index] = 0"
                          @change="book.tax[index] = 0"
                        />
                      </td>
                      <td>
                        <span v-if="!itemStatus[index]">{{ item.tax }}</span>
                        <input
                          v-else
                          class="form-control"
                          type="number"
                          min="0"
                          step="1"
                          v-model="book.tax[index]"
                          @input="book.taxPercent[index] = 0"
                          @change="book.taxPercent[index] = 0"
                        />
                      </td>
                      <td class="text-end">
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
                      <td v-if="!isCompleted">
                        <span v-if="!itemStatus[index]">
                          <a
                            class="me-3 dropset"
                            data-bs-toggle="dropdown"
                            aria-expanded="false"
                            href="javascript:void(0);"
                            ><img src="/img/icons/ellipise1.svg" alt="img"
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
                                @click="editItem(item.id, index)"
                                >Edit</a
                              >
                            </li>
                            <li>
                              <a
                                href="javascript:void(0);"
                                class="dropdown-item"
                                @click="deleteItem(item.id)"
                                >Delete</a
                              >
                            </li>
                          </ul>
                        </span>
                        <span v-else>
                          <a
                            style="font-size: larger"
                            class="btn btn-small btn-primary"
                            href="javascript:void(0);"
                            @click="
                              saveItem(
                                item.id,
                                index,
                                item.product,
                                item.salesOrder
                              )
                            "
                            ><i class="fa fa-save text-white"></i
                          ></a>
                        </span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="row">
              <div class="col-lg-6 col-sm-6 col-12">
                <div class="row">
                  <div class="col-lg-6 col-sm-6 col-12">
                    <div class="form-group">
                      <label>Order Tax</label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        step="0.01"
                        class="form-control"
                        v-model="salesorder.taxPercent"
                        required
                        :disabled="isCompleted"
                      />
                    </div>
                  </div>
                  <div class="col-lg-6 col-sm-6 col-12">
                    <div class="form-group">
                      <label>Discount</label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        step="0.01"
                        class="form-control"
                        v-model="salesorder.discountPercent"
                        required
                        :disabled="isCompleted"
                      />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-lg-6 col-sm-6 col-12">
                    <div class="form-group">
                      <label>Shipping</label>
                      <input
                        type="number"
                        class="form-control"
                        min="0"
                        step="0.01"
                        v-model="salesorder.shippingCost"
                        required
                        :disabled="isCompleted"
                      />
                    </div>
                  </div>
                  <div class="col-lg-6 col-sm-6 col-12">
                    <div class="form-group">
                      <label>Payment Status</label>
                      <select
                        class="form-select"
                        v-model="salesorder.paidStatus"
                        required
                        :disabled="isCompleted"
                      >
                        <option value="">Choose</option>
                        <option value="Unpaid">Unpaid</option>
                        <option value="Partial">Partial</option>
                        <option value="Paid">Paid</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-lg-12">
                    <div class="form-group">
                      <label>Description</label>
                      <textarea
                        class="form-control"
                        v-model="salesorder.desc"
                        :disabled="isCompleted"
                        style="
                          width: 100%;
                          height: 100%;
                          box-sizing: border-box;
                        "
                      ></textarea>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-6 col-sm-6 col-12">
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
                          <h5>₱ {{ salesorder.shippingCost }}</h5>
                        </li>
                        <li class="total">
                          <h4>Grand Total</h4>
                          <h5>₱ {{ netTotal }}</h5>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-lg-12">
                <button
                  type="submit"
                  class="btn btn-submit me-2"
                  :disabled="isCompleted"
                >
                  Submit
                </button>
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
          </form>
        </div>
      </div>
    </div>
  </div>
  <ToasterComponent ref="toast" />
</template>
<script>
import ToasterComponent from "../../common/ToasterComponent.vue";
import TableComponent from "../../common/TableComponent.vue";
import {
  salesOrderApi,
  salesItemApi,
  salesTransactionApi,
} from "@/services/salesServices";
import { peopleCustomerApi } from "@/services/peopleServices";
import { productItemApi } from "@/services/ProductServices";
export default {
  components: {
    ToasterComponent,
    TableComponent,
  },
  data() {
    return {
      currentId: null,
      isCompleted: false,
      partialTotal: 0,
      salestransaction: {
        refno: "",
        desc: "",
        cost: 0,
        balance: 0,
        amountPaid: 0,
        status: "",
        salesOrder: "",
      },
      salesorder: {
        customer: "",
        refno: "",
        salesDate: "",
        desc: "",
        discountPercent: 0,
        taxPercent: 0,
        shippingCost: 0,
        progressStatus: "",
        paidStatus: "",
      },
      cashDenominations: [
        {
          label: "+1.00",
          value: 1,
        },
        {
          label: "+5.00",
          value: 5,
        },
        {
          label: "+10.00",
          value: 10,
        },
        {
          label: "+20.00",
          value: 20,
        },
        {
          label: "+50.00",
          value: 50,
        },
        {
          label: "+100.00",
          value: 100,
        },
        {
          label: "+500.00",
          value: 500,
        },
        {
          label: "+1000.00",
          value: 1000,
        },
      ],
      headers: [
        {
          label: "",
          field: "checkbox",
          sortable: false,
        },
        {
          label: "Customer",
          field: "customerData",
          sortable: true,
        },
        {
          label: "Reference No.",
          field: "refno",
          sortable: true,
        },
        {
          label: "Date",
          field: "salesDate",
          sortable: true,
        },
        {
          label: "Status",
          field: "progressStatus",
          sortable: true,
          slot: true,
        },
        {
          label: "Payment Status",
          field: "paidStatus",
          sortable: true,
          slot: true,
        },
        {
          label: "Description",
          field: "desc",
          sortable: true,
        },
        {
          label: "Last Cost",
          field: "lastCost",
          sortable: true,
        },
        {
          label: "Total Paid",
          field: "totalPaid",
          sortable: true,
        },
        {
          label: "Last Balance",
          field: "lastBalance",
          sortable: true,
        },
        {
          label: "",
          field: "action",
          sortable: false,
          slot: true,
        },
      ],
      salesorders: [],
      salestransactions: [],
      transactionshistory: [],
      salesitems: [],
      customers: [],
      products: [],
      itemStatus: [],
      book: {
        qty: [],
        price: [],
        discountPercent: [],
        discount: [],
        taxPercent: [],
        tax: [],
      },
    };
  },
  computed: {
    subtotal() {
      return this.salesitems.reduce(
        (acc, item) => acc + parseFloat(item.totalCost),
        0
      );
    },
    taxCost() {
      return (this.subtotal * (this.salesorder.taxPercent / 100)).toFixed(2);
    },
    discountCost() {
      return (this.subtotal * (this.salesorder.discountPercent / 100)).toFixed(
        2
      );
    },
    netTotal() {
      return (
        this.subtotal +
        parseFloat(this.taxCost) -
        parseFloat(this.discountCost) +
        parseFloat(this.salesorder.shippingCost)
      ).toFixed(2);
    },
    grandTotal() {
      return (
        this.subtotal +
        parseFloat(this.taxCost) -
        parseFloat(this.discountCost) +
        parseFloat(this.salesorder.shippingCost) -
        parseFloat(this.partialTotal)
      ).toFixed(2);
    },
    filteredsalesorders() {
      return this.salesorders.map((o) => {
        const customerData =
          (o.customer_data && o.customer_data.name) || "Walk-in";
        return {
          ...o,
          customerData: customerData,
          salesDate: new Date(o.salesDate),
        };
      });
    },
    filteredtransactionshistory() {
      return this.transactionshistory.map((o) => {
        return {
          ...o,
          created: Intl.DateTimeFormat("en-US", {
            month: "2-digit",
            day: "2-digit",
            year: "numeric",
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
          }).format(new Date(o.created)),
        };
      });
    },
  },
  methods: {
    updateTotalCash() {
      if (
        this.salestransaction.amountPaid === 0 ||
        this.salestransaction.amountPaid.toString() === "" ||
        this.salestransaction.amountPaid === NaN
      ) {
        this.salestransaction.amountPaid = 0;
      } else {
        this.salestransaction.amountPaid =
          this.salestransaction.amountPaid.toString();
      }
      //alert(this.totalCash)
    },
    addToCash(d) {
      this.salestransaction.amountPaid = isNaN(
        parseFloat(this.salestransaction.amountPaid)
      )
        ? 0
        : parseFloat(this.salestransaction.amountPaid) + d;
    },
    getBadgeClass(status) {
      return {
        "bg-lightyellow": status === "On Progress" || status === "Partial",
        "bg-lightred": status === "Pending" || status === "Unpaid",
        "bg-lightgreen":
          status !== "On Progress" &&
          status !== "Pending" &&
          status !== "Partial" &&
          status !== "Unpaid",
      };
    },
    async loadItems() {
      this.customers = await peopleCustomerApi.fetchAll();
      this.products = await productItemApi.fetchAll();
      this.autocomplete(
        document.getElementById("productItems"),
        this.products.map((item) => item.name)
      );
    },
    async loadData() {
      this.salesorders = await salesOrderApi.fetchAll();
    },
    async loadTransactions() {
      this.salestransactions = await salesTransactionApi.fetchAll();
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
            autoCompleteItem.addEventListener("click", function () {
              inputField.value = this.getElementsByTagName("input")[0].value;
              vm.insertItem();
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
    calculateNewCost(index) {
      const qty = parseFloat(this.book.qty[index]);
      const price = parseFloat(this.book.price[index]);
      const discount = this.book.discount[index];
      const discountPercent = this.book.discountPercent[index] / 100;
      const tax = this.book.tax[index];
      const taxPercent = this.book.taxPercent[index] / 100;

      const totalCost = qty * price;
      const discountedTotalCost =
        discount === 0
          ? totalCost * (1 - discountPercent)
          : totalCost - discount;
      const taxedTotalCost =
        tax === 0
          ? discountedTotalCost * (1 + taxPercent)
          : discountedTotalCost - tax;
      return taxedTotalCost.toFixed(2);
    },
    async insertItem() {
      const query = document.getElementById("productItems").value;
      const isNotExist =
        this.products.every(
          (o) => !o.name.toLowerCase().includes(query.toLowerCase())
        ) ||
        this.salesitems.every(
          (o) => !o.productName.toLowerCase().includes(query.toLowerCase())
        );

      if (!isNotExist) {
        document.getElementById("productItems").value = "";
        return false;
      } else {
        const productData = this.products.find(
          (o) => o.name.toLowerCase() === query.toLowerCase()
        );
        const productId = productData?.id || -1;
        const productPrice = productData?.price || 0;
        const productMaxQty = productData?.qty || 0;
        const productMinQty = productData?.minqty || 0;

        if (productPrice > 0) {
          const data = {
            productName: query,
            productMaxQty: parseFloat(productMaxQty),
            productMinQty: parseFloat(productMinQty),
            qty: 1,
            price: parseFloat(productPrice),
            discount: 0,
            discountPercent: 0,
            tax: 0,
            taxPercent: 0,
            totalCost: 0,
            product: productId,
            salesOrder: this.currentId,
            id: -1,
          };
          this.salesitems.unshift(data);
          this.itemStatus.unshift(true);
          [
            "qty",
            "price",
            "discountPercent",
            "discount",
            "taxPercent",
            "tax",
          ].forEach((prop) => {
            const entry =
              prop === "price"
                ? parseFloat(productPrice)
                : prop === "qty"
                ? 1
                : 0;
            this.book[prop].unshift(entry);
          });
        } else {
          this.$refs.toast.showToast(
            "danger",
            "Price is out of range. Please check product item!"
          );
        }
      }

      document.getElementById("productItems").value = "";
    },
    async editItem(id, index) {
      this.itemStatus[index] = true;
    },
    async saveItem(id, index, prd, po) {
      this.itemStatus[index] = false;
      const getValue = (property) => this.book?.[property]?.[index] ?? 0;

      const newitem = this.salesitems.find((o) => o.id === id) || {};
      const properties = [
        "qty",
        "price",
        "discountPercent",
        "discount",
        "taxPercent",
        "tax",
      ];

      properties.forEach((prop) => (newitem[prop] = getValue(prop)));
      newitem.totalCost = this.calculateNewCost(index);
      const requestData = {
        product: prd,
        salesOrder: po,
        totalCost: newitem.totalCost,
        ...Object.fromEntries(properties.map((prop) => [prop, newitem[prop]])),
      };

      if (id !== -1) {
        await salesItemApi.edit(id, requestData);
      } else {
        await salesItemApi.add(requestData);
      }

      const transhistory = await salesTransactionApi.filter({
        columnName: "salesOrder",
        columnKey: this.currentId,
      });
      this.partialTotal = transhistory.reduce(
        (acc, item) => acc + parseFloat(item.amountPaid),
        0
      );
      this.transactionshistory = transhistory.sort((a, b) => {
        return new Date(b.created) - new Date(a.created);
      });
      this.salesorder.totalPaid = this.partialTotal;
      this.salesorder.lastCost = this.netTotal;
      this.salesorder.lastBalance = this.grandTotal;
      await salesOrderApi.edit(this.currentId, this.salesorder);
      this.loadData();
    },
    async deleteItem(id) {
      const result = await this.$swal.fire({
        icon: "warning",
        title: "Are you sure?",
        text: "Once deleted, you will not be able to recover this item!",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        showCancelButton: true,
      });

      if (result.isConfirmed) {
        const index = this.salesitems.findIndex((o) => o.id === id);
        this.salesitems.splice(index, 1);
        await salesItemApi.delete(id);
      }
    },
    async saveAction() {
      const received = this.salesorder.progressStatus === "Completed";
      const confirmation = received
        ? await this.$swal.fire({
            icon: "warning",
            title: "Confirm Status Change to 'Completed'",
            text: "Proceeding will finalize the status as 'Completed', and you won't be able to edit this sales items later.",
            confirmButtonText: "Yes",
            cancelButtonText: "No",
            showCancelButton: true,
          })
        : { isConfirmed: true };

      if (!confirmation?.isConfirmed) return false;

      if (received) {
        for (const item of this.salesitems) {
          const data = await productItemApi.fetchOne(item.product);
          const product_data = {
            ...data,
            qty:
              parseFloat(data.qty) -
              parseFloat(
                this.book.qty[
                  this.salesitems.findIndex((o) => o.productName === data.name)
                ]
              ),
          };
          await productItemApi.edit(item.product, product_data);
        }
      }

      jQuery("#editModal").modal("toggle");
      const transhistory = await salesTransactionApi.filter({
        columnName: "salesOrder",
        columnKey: this.currentId,
      });
      this.partialTotal = transhistory.reduce(
        (acc, item) => acc + parseFloat(item.amountPaid),
        0
      );
      this.transactionshistory = transhistory.sort((a, b) => {
        return new Date(b.created) - new Date(a.created);
      });
      this.salesorder.totalPaid = this.partialTotal;
      this.salesorder.lastCost = this.netTotal;
      this.salesorder.lastBalance = this.grandTotal;
      await salesOrderApi.edit(this.currentId, this.salesorder);
      this.loadData();
    },
    async payAction(id) {
      jQuery("#payModal").modal("toggle");
      this.salestransaction = {
        refno: "",
        desc: "",
        cost: 0,
        balance: 0,
        amountPaid: 0,
        status: "",
        salesOrder: id,
      };
      const transhistory = await salesTransactionApi.filter({
        columnName: "salesOrder",
        columnKey: id,
      });
      this.partialTotal = transhistory.reduce(
        (acc, item) => acc + parseFloat(item.amountPaid),
        0
      );
      this.transactionshistory = transhistory.sort((a, b) => {
        return new Date(b.created) - new Date(a.created);
      });
      this.editCommand(id);
    },
    async payOrder() {
      if (
        parseFloat(this.salestransaction.amountPaid) <= 0 ||
        parseFloat(this.salestransaction.amountPaid) >
          parseFloat(this.grandTotal)
      ) {
        this.$refs.toast.showToast("danger", "Invalid tendered amount paid!");
        return false;
      }
      await salesTransactionApi
        .filter({
          columnName: "refno",
          columnKey: this.salestransaction.refno,
        })
        .then(async (result) => {
          if (result.length > 0) {
            this.$refs.toast.showToast(
              "danger",
              "Sales transaction with this reference no. already exists."
            );
            return false;
          } else {
            this.salestransaction.cost = this.netTotal;
            this.salestransaction.balance = (
              parseFloat(this.grandTotal) -
              parseFloat(this.salestransaction.amountPaid)
            ).toFixed(2);
            this.salestransaction.status =
              parseFloat(this.salestransaction.balance) === 0
                ? "full"
                : "partial";
            await salesTransactionApi.add(this.salestransaction);
            this.salestransaction.refno = "";
            this.salestransaction.desc = "";
            this.salestransaction.amountPaid = 0;
            this.salesorder.paidStatus =
              this.salestransaction.status === "partial" ? "Partial" : "Paid";
            this.loadTransactions();
            const transhistory = await salesTransactionApi.filter({
              columnName: "salesOrder",
              columnKey: this.currentId,
            });
            this.partialTotal = transhistory.reduce(
              (acc, item) => acc + parseFloat(item.amountPaid),
              0
            );
            this.transactionshistory = transhistory.sort((a, b) => {
              return new Date(b.created) - new Date(a.created);
            });
            this.salesorder.totalPaid = this.partialTotal;
            this.salesorder.lastCost = this.netTotal;
            this.salesorder.lastBalance = this.grandTotal;
            await salesOrderApi.edit(this.currentId, this.salesorder);
            this.loadData();
          }
        });
    },
    async editCommand(id) {
      this.currentId = id;
      const salesitems = await salesItemApi.filter({
        columnName: "salesOrder_id",
        columnKey: id,
      });
      this.salesitems = salesitems.map((o) => ({
        ...o,
        productName: o.product_data.name,
      }));
      this.isCompleted =
        this.salesorders.find((o) => o.id === id).progressStatus ===
        "Completed";
      this.itemStatus = Array(this.salesitems.length).fill(false);

      this.book = [
        "qty",
        "price",
        "discountPercent",
        "discount",
        "taxPercent",
        "tax",
      ].reduce((acc, key) => {
        acc[key] = this.salesitems.map((item) => item[key]);
        return acc;
      }, {});

      const {
        customer,
        refno,
        salesDate,
        desc,
        discountPercent,
        taxPercent,
        shippingCost,
        progressStatus,
        paidStatus,
      } = await salesOrderApi.fetchOne(id);
      this.salesorder = {
        customer: customer === null ? "" : customer,
        refno,
        salesDate: new Date(salesDate).toISOString().split("T")[0],
        desc,
        discountPercent,
        taxPercent,
        shippingCost,
        progressStatus,
        paidStatus,
      };
    },
    editAction(id) {
      jQuery("#editModal").modal("toggle");
      this.editCommand(id);
    },
  },
  async mounted() {
    this.loadItems();
    this.loadTransactions();
    this.loadData();
  },
};
</script>
<style></style>
