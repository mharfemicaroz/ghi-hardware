<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Product List</h4>
      <h6>Manage your products</h6>
    </div>
    <div class="page-btn">
      <router-link
        class="btn btn-added"
        @click="navigateTo('/index/addproduct')"
        to="/index/addproduct"
      >
        <img src="/img/icons/plus.svg" alt="img" class="me-1" />Add New Product
      </router-link>
    </div>
  </div>
  <div class="tabs-set">
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button
          class="nav-link active"
          id="tab1-tab"
          data-bs-toggle="tab"
          data-bs-target="#tab1"
          type="button"
          role="tab"
          aria-controls="tab1"
          aria-selected="true"
        >
          Available
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="tab2-tab"
          data-bs-toggle="tab"
          data-bs-target="#tab2"
          type="button"
          role="tab"
          aria-controls="tab2"
          aria-selected="false"
        >
          For Pricing
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="tab3-tab"
          data-bs-toggle="tab"
          data-bs-target="#tab3"
          type="button"
          role="tab"
          aria-controls="tab3"
          aria-selected="false"
        >
          Expiring
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="tab4-tab"
          data-bs-toggle="tab"
          data-bs-target="#tab4"
          type="button"
          role="tab"
          aria-controls="tab4"
          aria-selected="false"
        >
          For Purchase
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="tab5-tab"
          data-bs-toggle="tab"
          data-bs-target="#tab5"
          type="button"
          role="tab"
          aria-controls="tab5"
          aria-selected="false"
        >
          Unavailable
        </button>
      </li>
    </ul>
    <div class="tab-content" id="myTabContent">
      <div
        class="tab-pane fade show active"
        id="tab1"
        role="tabpanel"
        aria-labelledby="tab1-tab"
      >
        <TableComponent
          :mainHeaders="headers"
          :mainItems="
            filteredproducts.filter(
              (o) => o.status === 'open' && !o.isRecentPurchased
            )
          "
          :editable="false"
          :moreAction="true"
          :actionBtns="['Edit Product', 'View/Set Price', 'Add Voucher']"
          @btn-action1="editAction"
          @btn-action2="viewPrice"
          @btn-action3="addVoucher"
        />
      </div>
      <div
        class="tab-pane fade"
        id="tab2"
        role="tabpanel"
        aria-labelledby="tab2-tab"
      >
        <TableComponent
          :mainHeaders="headerswcheckbox"
          :mainItems="
            filteredproducts.filter(
              (o) => o.status === 'open' && o.isRecentPurchased
            )
          "
          :editable="false"
          :moreAction="true"
          :actionBtns="['Edit Product', 'View/Set Price', 'Add Voucher']"
          @btn-action1="editAction"
          @btn-action2="viewPrice"
          @btn-action3="addVoucher"
          :selectable="true"
          :batchAction="true"
        >
          <template #checkboxtrigger="data">
            <button
              type="button"
              class="btn btn-sm btn-primary text-white"
              @click="batchAction(data.data.dt)"
            >
              Batch Price Setting
            </button>
          </template>
        </TableComponent>
      </div>
      <div
        class="tab-pane fade"
        id="tab3"
        role="tabpanel"
        aria-labelledby="tab3-tab"
      >
        <TableComponent
          :mainHeaders="extendheaders"
          :mainItems="expiredfilteredproducts"
          :editable="false"
          :moreAction="true"
          :actionBtns="['Edit Product', 'View/Set Price']"
          @btn-action1="editAction"
          @btn-action2="viewPrice"
        />
      </div>
      <div
        class="tab-pane fade"
        id="tab4"
        role="tabpanel"
        aria-labelledby="tab4-tab"
      >
        <div class="col-lg-4">
          <div class="form-group">
            <select class="form-select" v-model="threshold" required>
              <option value="">
                Choose the inventory quantity threshold percentage
              </option>
              <option value="0">0%</option>
              <option value="5">5%</option>
              <option value="10">10%</option>
              <option value="20">20%</option>
              <option value="30">30%</option>
              <option value="40">40%</option>
              <option value="50">50%</option>
              <option value="60">60%</option>
              <option value="70">70%</option>
              <option value="80">80%</option>
              <option value="90">90%</option>
              <option value="100">100%</option>
            </select>
          </div>
        </div>

        <TableComponent
          :mainHeaders="headers"
          :mainItems="forpurchasedfilteredproducts"
          :editable="false"
          :moreAction="true"
          :actionBtns="['Edit Product', 'View/Set Price']"
          @btn-action1="editAction"
          @btn-action2="viewPrice"
        />
      </div>
      <div
        class="tab-pane fade"
        id="tab5"
        role="tabpanel"
        aria-labelledby="tab5-tab"
      >
        <TableComponent
          :mainHeaders="headers"
          :mainItems="filteredproducts.filter((o) => o.status !== 'open')"
          :editable="false"
          :moreAction="true"
          :actionBtns="['Edit Product', 'View/Set Price']"
          @btn-action1="editAction"
          @btn-action2="viewPrice"
        />
      </div>
    </div>
  </div>
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
          <h4 class="modal-title" id="editModalLabel">Edit Product</h4>
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
          <form @submit.prevent="saveAction">
            <div class="row">
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Product Name</label>
                  <input type="text" v-model="product.name" required />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Category</label>
                  <select
                    class="form-select"
                    v-model="product.category"
                    @change="toggleSelect"
                    required
                  >
                    <option
                      v-for="(item, index) in categories"
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
                  <label>Sub Category</label>
                  <select
                    v-if="filteredSubcategories.length > 0"
                    class="form-select"
                    v-model="product.subcategory"
                    required
                  >
                    <option
                      v-for="(item, index) in filteredSubcategories"
                      :key="index"
                      :value="item.id"
                    >
                      {{ item.name }}
                    </option>
                  </select>
                  <input
                    v-else
                    type="text"
                    value="Not Available"
                    class="form-control"
                    readonly
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Brand</label>
                  <select class="form-select" v-model="product.brand">
                    <option value="">No Brand</option>
                    <option
                      v-for="(item, index) in brands"
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
                  <label>Unit</label>
                  <select class="form-select" v-model="product.unit" required>
                    <option value="pc">Piece</option>
                    <option value="kg">Kilogram</option>
                    <option value="m">Meter</option>
                    <option value="sqm">Square Meter</option>
                    <option value="cum">Cubic Meter</option>
                    <option value="qty">Quantity</option>
                  </select>
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>SKU</label>
                  <input type="text" v-model="product.sku" required />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Minimum Qty</label>
                  <input
                    type="number"
                    class="form-control"
                    min="0"
                    step="1"
                    required
                    v-model="product.minqty"
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Quantity</label>
                  <input
                    type="number"
                    class="form-control"
                    :min="product.minqty"
                    required
                    step="1"
                    v-model="product.qty"
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Manufacturing Date </label>
                  <div class="input-groupicon">
                    <input
                      type="date"
                      class="form-control"
                      v-model="product.manufacturingDate"
                    />
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Expiration Date </label>
                  <div class="input-groupicon">
                    <input
                      type="date"
                      class="form-control"
                      v-model="product.expirationDate"
                    />
                  </div>
                </div>
              </div>
              <div class="col-lg-6 col-sm-6 col-12">
                <div class="form-group">
                  <label>Description</label>
                  <input type="text" v-model="product.desc" required />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Tax</label>
                  <input
                    type="number"
                    class="form-control"
                    min="0"
                    required
                    step="0.01"
                    v-model="product.tax"
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Discount</label>
                  <input
                    type="number"
                    class="form-control"
                    min="0"
                    required
                    step="0.01"
                    v-model="product.discount"
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Price</label>
                  <input
                    type="number"
                    class="form-control"
                    :min="product.sellingPrice"
                    required
                    step="0.01"
                    v-model="product.price"
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label> Status</label>
                  <select class="form-select" v-model="product.status" required>
                    <option value="closed">Closed</option>
                    <option value="open">Open</option>
                  </select>
                </div>
              </div>
              <div class="col-lg-12">
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
              </div>
              <div class="col-lg-12">
                <button type="submit" class="btn btn-submit me-2">
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
  <div
    class="modal fade show"
    id="batchpriceModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="batchpriceModalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="batchpriceModalLabel">
            Batch Price Setting Module
          </h4>
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
            <div class="col-lg-9 col-sm-6 col-12">
              <div
                class="table-responsive"
                style="
                  height: fit-content;
                  max-height: 300px;
                  overflow-y: auto;
                  overflow-x: hidden;
                "
              >
                <table class="table">
                  <thead>
                    <tr>
                      <th>Item</th>
                      <th>Price</th>
                      <th>Selling Price</th>
                      <th>Profit</th>
                      <th>Markup %</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item of filteredbatchitems">
                      <td>{{ item.name }}</td>
                      <td>{{ item.price }}</td>
                      <td>{{ item.sellingPrice }}</td>
                      <td>{{ item.difference }}</td>
                      <td>{{ item.percentage }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="col-lg-3 col-sm-6 col-12">
              <form id="priceForm" @submit.prevent="setMarkup">
                <div class="row">
                  <div class="col-lg-12 float-md-right mb-0">
                    <div class="total-order mb-0 mt-0">
                      <ul>
                        <li class="markup" @click="newmarkup = 5">
                          <h4>Markup @ 5%</h4>
                          <h5>-</h5>
                        </li>
                        <li class="markup" @click="newmarkup = 10">
                          <h4>Markup @ 10%</h4>
                          <h5>-</h5>
                        </li>
                        <li class="markup" @click="newmarkup = 20">
                          <h4>Markup @ 20%</h4>
                          <h5>-</h5>
                        </li>
                        <li class="markup" @click="newmarkup = 30">
                          <h4>Markup @ 30%</h4>
                          <h5>-</h5>
                        </li>
                        <li class="markup" @click="newmarkup = 40">
                          <h4>Markup @ 40%</h4>
                          <h5>-</h5>
                        </li>
                        <li class="markup" @click="newmarkup = 50">
                          <h4>Markup @ 50%</h4>
                          <h5>-</h5>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="form-group">
                    <label>Markup</label>
                    <input
                      type="number"
                      class="form-control"
                      min="0"
                      max="100"
                      step="0.01"
                      v-model="newmarkup"
                      required
                    />
                  </div>
                </div>
                <div class="col-lg-12">
                  <button type="submit" class="btn btn-submit me-2">Set</button>
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
  <div
    class="modal fade show"
    id="priceModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="priceModalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="priceModalLabel">Price Module</h4>
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
            <div class="col-lg-9 col-sm-6 col-12">
              <div
                class="table-responsive"
                style="
                  height: fit-content;
                  max-height: 300px;
                  overflow-y: auto;
                  overflow-x: hidden;
                "
              >
                <table class="table">
                  <thead>
                    <tr>
                      <th>Last Date Purchased</th>
                      <th>Price</th>
                      <th>Selling Price</th>
                      <th>Profit</th>
                      <th>Markup %</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item of pricehistory">
                      <td>{{ item.created }}</td>
                      <td>{{ item.price }}</td>
                      <td>{{ item.sellingPrice }}</td>
                      <td>{{ item.difference }}</td>
                      <td>{{ item.percentage }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="col-lg-3 col-sm-6 col-12">
              <form id="priceForm" @submit.prevent="setPrice">
                <div class="row">
                  <div class="col-lg-12 float-md-right mb-0">
                    <div class="total-order mb-0 mt-0">
                      <ul>
                        <li
                          class="markup"
                          @click="
                            newprice = parseFloat(
                              (product.purchasePrice * 1.05).toFixed(2)
                            )
                          "
                        >
                          <h4>Markup @ 5%</h4>
                          <h5>
                            ₱{{ (product.purchasePrice * 1.05).toFixed(2) }}
                          </h5>
                        </li>
                        <li
                          class="markup"
                          @click="
                            newprice = parseFloat(
                              (product.purchasePrice * 1.1).toFixed(2)
                            )
                          "
                        >
                          <h4>Markup @ 10%</h4>
                          <h5>
                            ₱{{ (product.purchasePrice * 1.1).toFixed(2) }}
                          </h5>
                        </li>
                        <li
                          class="markup"
                          @click="
                            newprice = parseFloat(
                              (product.purchasePrice * 1.2).toFixed(2)
                            )
                          "
                        >
                          <h4>Markup @ 20%</h4>
                          <h5>
                            ₱{{ (product.purchasePrice * 1.2).toFixed(2) }}
                          </h5>
                        </li>
                        <li
                          class="markup"
                          @click="
                            newprice = parseFloat(
                              (product.purchasePrice * 1.3).toFixed(2)
                            )
                          "
                        >
                          <h4>Markup @ 30%</h4>
                          <h5>
                            ₱{{ (product.purchasePrice * 1.3).toFixed(2) }}
                          </h5>
                        </li>
                        <li
                          class="markup"
                          @click="
                            newprice = parseFloat(
                              (product.purchasePrice * 1.5).toFixed(2)
                            )
                          "
                        >
                          <h4>Markup @ 50%</h4>
                          <h5>
                            ₱{{ (product.purchasePrice * 1.5).toFixed(2) }}
                          </h5>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="form-group">
                    <label>Price</label>
                    <input
                      type="number"
                      class="form-control"
                      :min="product.purchasePrice"
                      step="0.01"
                      v-model="newprice"
                      required
                    />
                  </div>
                </div>
                <div class="col-lg-12">
                  <button type="submit" class="btn btn-submit me-2">Set</button>
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
  <div
    class="modal fade show"
    id="voucherModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="voucherModalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="voucherModalLabel">Voucher(s) Module</h4>
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
            <div class="col-lg-9 col-sm-6 col-12">
              <div
                class="table-responsive"
                style="
                  height: fit-content;
                  max-height: 300px;
                  overflow-y: auto;
                  overflow-x: hidden;
                "
              >
                <table class="table">
                  <thead>
                    <tr>
                      <th>Name</th>
                      <th>Desc</th>
                      <th>Code</th>
                      <th>Start Date</th>
                      <th>Expiration Date</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item of voucherlists">
                      <td>{{ item.name }}</td>
                      <td>{{ item.desc }}</td>
                      <td>{{ item.code }}</td>
                      <td>{{ item.startDate }}</td>
                      <td>{{ item.expirationDate }}</td>
                      <td>
                        <button
                          class="btn btn-small badge badge-pill btn-danger"
                          type="button"
                          @click="deleteVoucherItem(item.id)"
                        >
                          <i class="fa fa-times"></i>
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="col-lg-3 col-sm-6 col-12">
              <form id="voucherForm" @submit.prevent="setVoucher">
                <div class="row">
                  <div class="form-group">
                    <label>Voucher</label>
                    <select class="form-control" v-model="voucher" required>
                      <option value="">Choose</option>
                      <option
                        v-for="(item, index) in filteredvouchers"
                        :key="index"
                        :value="item.id"
                      >
                        {{ item.code }}
                      </option>
                    </select>
                  </div>
                </div>
                <div class="col-lg-12">
                  <button type="submit" class="btn btn-submit me-2">Add</button>
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
</template>
<script>
import ToasterComponent from "../../common/ToasterComponent.vue";
import TableComponent from "../../common/TableComponent.vue";
import {
  productSubCategoryApi,
  productCategoryApi,
  productBrandApi,
  productItemApi,
  productVoucherApi,
  productVoucherItemApi,
} from "@/services/productServices";
import { purchaseItemApi } from "@/services/purchaseServices";
export default {
  components: {
    ToasterComponent,
    TableComponent,
  },
  data() {
    return {
      productId: null,
      threshold: 0,
      product: {
        category: "",
        subcategory: "",
        brand: "",
        name: "",
        desc: "",
        unit: "",
        sku: "",
        minqty: 0,
        qty: 0,
        tax: 0,
        discount: 0,
        price: 0,
        status: "",
        manufacturingDate: "",
        expirationDate: "",
        latestPrice: 0,
      },
      headers: [
        {
          label: "Item",
          field: "name",
          sortable: true,
        },
        {
          label: "Category",
          field: "categoryName",
          sortable: true,
        },
        {
          label: "Sub-category",
          field: "subcategoryName",
          sortable: true,
        },
        {
          label: "Brand",
          field: "brandName",
          sortable: true,
        },
        {
          label: "SKU",
          field: "sku",
          sortable: true,
        },
        {
          label: "Qty",
          field: "qty",
          sortable: true,
        },
        {
          label: "Price",
          field: "price",
          sortable: true,
        },
        {
          label: "Description",
          field: "desc",
          sortable: true,
        },
        {
          label: "",
          field: "action",
          sortable: false,
        },
      ],
      pricehistory: [],
      categories: [],
      subcategories: [],
      brands: [],
      products: [],
      batchitems: [],
      vouchers: [],
      voucherlists: [],
      imageFile: null,
      imageFileName: "",
      voucher: "",
      newprice: 0,
      newmarkup: 0,
    };
  },
  computed: {
    filteredSubcategories() {
      return this.subcategories.filter((item) => {
        return item.category === this.product.category;
      });
    },
    headerswcheckbox() {
      return [
        {
          label: "",
          field: "checkbox",
          sortable: false,
        },
        ...this.headers,
      ];
    },
    extendheaders() {
      const indexToInsertBefore = this.headers.length - 1;
      return [
        ...this.headers.slice(0, indexToInsertBefore),
        {
          label: "Expired in",
          field: "expiredin",
          sortable: true,
        },
        ...this.headers.slice(indexToInsertBefore),
      ];
    },
    filteredvouchers() {
      return this.vouchers.map((o) => {
        let code = "";

        if (o.discountPercentage == 0 && o.discount == 0) {
          code = `Special Price Offer: ${parseFloat(o.specialPrice)}`;
        } else if (o.discount == 0 && o.specialPrice == 0) {
          code = `Flexi - ${parseFloat(o.discountPercentage)}% off`;
        } else if (o.specialPrice == 0 && o.discountPercentage == 0) {
          code = `Fix - ${o.discount} off`;
        } else {
          // Handle other cases here if needed
          code = "Other Case";
        }
        return {
          ...o,
          code: "(" + o.name + ") " + code,
        };
      });
    },
    filteredbatchitems() {
      return this.batchitems.map((item) => {
        const sellingPrice = (
          item.price *
          (1 + parseFloat(this.newmarkup / 100))
        ).toFixed(2);
        const percentage = this.newmarkup.toFixed(2);
        const difference = (
          parseFloat(sellingPrice) - parseFloat(item.price)
        ).toFixed(2);
        return {
          ...item,
          sellingPrice: sellingPrice,
          percentage: percentage,
          difference: difference,
        };
      });
    },
    filteredproducts() {
      return this.products
        .map((o) => {
          const categoryName = o.category_data.name;
          const subcategoryName = o.subcategory_data.name;
          const brandName =
            o.brand_data !== null ? o.brand_data.name : "No Brand";

          return {
            ...o,
            categoryName: categoryName,
            subcategoryName: subcategoryName,
            brandName: brandName,
          };
        })
        .sort((a, b) => {
          const p = a.name;
          const q = b.name;
          if (p < q) {
            return -1;
          }
          if (p > q) {
            return 1;
          }
          return 0;
        });
    },
    forpurchasedfilteredproducts() {
      if (this.threshold === "") {
        return [];
      }
      return this.filteredproducts
        .map((o) => {
          const threshold = Math.floor(
            parseFloat(o.minqty) +
              (parseFloat(o.qty) + 1) *
                (parseFloat(this.threshold) === 0
                  ? 0
                  : parseFloat(this.threshold) / 100)
          );
          return {
            ...o,
            threshold: threshold,
          };
        })
        .filter((o) => parseFloat(o.qty) <= parseFloat(o.threshold));
    },
    expiredfilteredproducts() {
      const today = new Date(new Date().setHours(0, 0, 0, 0));
      const sevenDaysLater = new Date(today);
      sevenDaysLater.setDate(today.getDate() + 7);

      return this.filteredproducts
        .filter((o) => {
          const isOpen = o.status === "open";
          const isExpiringWithin7Days =
            new Date(new Date(o.expirationDate).setHours(0, 0, 0, 0)) <=
              sevenDaysLater &&
            new Date(new Date(o.expirationDate).setHours(0, 0, 0, 0)) >= today;

          return isOpen && isExpiringWithin7Days;
        })
        .map((o) => {
          const expiredin = Math.floor(
            (new Date(o.expirationDate) - new Date()) / (1000 * 60 * 60 * 24)
          );
          return {
            ...o,
            expiredin: expiredin + " day(s)",
          };
        });
    },
  },
  methods: {
    toggleSelect() {
      if (this.filteredSubcategories.length === 0) {
        this.subcategory = null;
      }
    },
    navigateTo(path, propSidebar = true) {
      // Adding a unique timestamp as a query parameter to force reload

      // Saving path to localStorage
      const isSidebar = propSidebar || true;
      localStorage.setItem("savedPath", path);
      localStorage.setItem("propSidebar", isSidebar);
      this.$router.push(path);
    },
    async deleteVoucherItem(id) {
      await productVoucherItemApi.delete(id);
      this.viewVoucher();
    },
    async setVoucher() {
      const response = await productVoucherItemApi.filter([
        {
          columnName: "product_id",
          columnKey: this.productId,
        },
        {
          columnName: "voucher_id",
          columnKey: this.voucher,
        },
      ]);
      if (response.length > 0) {
        this.$refs.toast.showToast(
          "danger",
          "Using the same voucher on the same item is not allowed."
        );
        return false;
      }
      await productVoucherItemApi.add({
        product: this.productId,
        voucher: this.voucher,
      });
      this.voucher = "";
      this.viewVoucher();
    },
    getBadgeClass(status) {
      return {
        "bg-lightgreen": status === true || status === "open",
        "bg-lightred": status === false || status === "close",
      };
    },
    async viewVoucher() {
      this.voucherlists = (
        await productVoucherItemApi.filter({
          columnName: "product_id",
          columnKey: this.productId,
        })
      )
        .map((o) => {
          let code = "";

          if (
            o.voucher_data.discountPercentage == 0 &&
            o.voucher_data.discount == 0
          ) {
            code = `Special Price Offer: ${parseFloat(
              o.voucher_data.specialPrice
            )}`;
          } else if (
            o.voucher_data.discount == 0 &&
            o.voucher_data.specialPrice == 0
          ) {
            code = `Flexi - ${parseFloat(
              o.voucher_data.discountPercentage
            )}% off`;
          } else if (
            o.voucher_data.specialPrice == 0 &&
            o.voucher_data.discountPercentage == 0
          ) {
            code = `Fix - ${o.voucher_data.discount} off`;
          } else {
            // Handle other cases here if needed
            code = "Other Case";
          }
          return {
            ...o,
            name: o.voucher_data.name,
            desc: o.voucher_data.desc,
            startDate: o.voucher_data.startDate.replace("T00:00:00Z", ""),
            expirationDate: o.voucher_data.expirationDate.replace(
              "T00:00:00Z",
              ""
            ),
            discountPercentage: o.voucher_data.discountPercentage,
            discount: o.voucher_data.discount,
            specialPrice: o.voucher_data.specialPrice,
            code: "(" + o.voucher_data.name + ") " + code,
          };
        })
        .sort((a, b) => {
          return new Date(a.expirationDate) - new Date(b.expirationDate);
        });
    },
    async addVoucher(id) {
      jQuery("#voucherModal").modal("toggle");
      this.productId = id;
      this.viewVoucher();
    },
    async setPrice() {
      jQuery("#priceModal").modal("toggle");
      this.product.price = this.newprice;
      this.product.isRecentPurchased = false;
      await productItemApi.edit(this.productId, this.product);
      const data = await purchaseItemApi.filter({
        columnName: "product_id",
        columnKey: this.productId,
      });
      const purchasedata = data.sort((a, b) => {
        return new Date(b.created) - new Date(a.created);
      })[0];
      const purchaseItemID = purchasedata.id;
      await purchaseItemApi.edit(purchaseItemID, {
        ...purchasedata,
        sellingPrice: this.newprice,
      });
      this.loadData();
    },
    async setMarkup() {
      for (const item of this.batchitems) {
        const productData = await productItemApi.fetchOne(item.product_id);
        const newprice = item.price * (1 + parseFloat(this.newmarkup) / 100);
        productData.price = newprice;
        productData.isRecentPurchased = false;
        await productItemApi.edit(item.product_id, productData);

        const purchasedata = await purchaseItemApi.fetchOne(item.id);
        purchasedata.sellingPrice = newprice;
        await purchaseItemApi.edit(item.id, purchasedata);
      }
      this.loadData();
      jQuery("#batchpriceModal").modal("toggle");
    },
    async batchAction(items) {
      this.newmarkup = 0;
      this.batchitems = [];
      for (const id of items) {
        const response = await purchaseItemApi.filter({
          columnName: "product_id",
          columnKey: id,
        });
        const purchasedata = response.sort((a, b) => {
          return new Date(b.created) - new Date(a.created);
        });
        if (purchasedata.length > 0) {
          const recentData = purchasedata[0];
          const productName = this.products.find((o) => o.id === id).name;
          this.batchitems.push({
            id: recentData.id,
            product_id: id,
            name: productName,
            price: recentData.price,
            sellingPrice: 0,
            difference: 0,
            percentage: 0,
          });
        }
      }
      jQuery("#batchpriceModal").modal("toggle");
    },
    async viewPrice(id) {
      const response = await productItemApi.fetchOne(id);
      this.product = {
        id: response.id,
        name: response.name,
        desc: response.desc,
        unit: response.unit,
        sku: response.sku,
        minqty: response.minqty,
        qty: response.qty,
        tax: response.tax,
        discount: response.discount,
        price: response.price,
        status: response.status,
        category: response.category,
        subcategory: response.subcategory || "",
        brand: response.brand || "",
      };
      const purchasedata = (
        await purchaseItemApi.filter({
          columnName: "product_id",
          columnKey: id,
        })
      ).sort((a, b) => {
        return new Date(b.created) - new Date(a.created);
      });
      if (purchasedata.length > 0) {
        jQuery("#priceModal").modal("toggle");
        this.newprice = parseFloat(this.product.price);
        this.productId = id;
        this.product.purchasePrice = purchasedata[0].price;
        this.pricehistory = purchasedata.map((o) => {
          const difference = parseFloat(o.sellingPrice) - parseFloat(o.price);
          const percentage =
            Math.round(
              ((parseFloat(o.sellingPrice) - parseFloat(o.price)) /
                parseFloat(o.price)) *
                10000
            ) / 100;
          return {
            ...o,
            difference: difference < 0 ? "-" : difference,
            percentage: isNaN(percentage)
              ? "-"
              : percentage < 0
              ? "-"
              : percentage,
          };
        });
      } else {
        this.pricehistory = [];
        this.$refs.toast.showToast(
          "warning",
          "This product has no recent purchases."
        );
      }
    },
    async saveAction() {
      jQuery("#editModal").modal("toggle");
      await productItemApi.edit(this.productId, this.product);
      this.loadData();
    },
    async editAction(id) {
      jQuery("#editModal").modal("toggle");
      this.productId = id;
      const result = (
        await purchaseItemApi.filter({
          columnName: "product_id",
          columnKey: id,
        })
      ).sort((a, b) => {
        return new Date(b.created) - new Date(a.created);
      });
      const latestPrice = result.length > 0 ? result[0].sellingPrice : 0;
      const response = await productItemApi.fetchOne(id);
      this.product = {
        id: response.id,
        name: response.name,
        desc: response.desc,
        unit: response.unit,
        sku: response.sku,
        minqty: response.minqty,
        qty: response.qty,
        tax: response.tax,
        discount: response.discount,
        price: response.price,
        sellingPrice: latestPrice,
        status: response.status,
        category: response.category,
        subcategory: response.subcategory || "",
        brand: response.brand || "",
        manufacturingDate: response.manufacturingDate
          ? response.manufacturingDate.toString().replace("T00:00:00Z", "")
          : null,
        expirationDate: response.expirationDate
          ? response.expirationDate.toString().replace("T00:00:00Z", "")
          : null,
      };
    },
    async loadData() {
      this.products = await productItemApi.fetchAll();
    },
  },
  async mounted() {
    this.categories = await productCategoryApi.fetchAll();
    this.subcategories = await productSubCategoryApi.fetchAll();
    this.brands = await productBrandApi.fetchAll();
    this.vouchers = await productVoucherApi.fetchAll();
    this.loadData();
  },
};
</script>
<style scoped>
.markup {
  cursor: pointer;
}
</style>
