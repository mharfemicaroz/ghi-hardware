import { createRouter, createWebHistory, createWebHashHistory } from "vue-router";
import SignIn from "../auth/SigninPage.vue";
import IndexPage from "../main/IndexPage.vue";
import DashboardPage from '../main/DashboardPage.vue';
import ProductList from '../main/Products/ProductList.vue';
import AddProduct from '../main/Products/AddProduct.vue';
import EditProduct from '../main/Products/EditProduct.vue';
import ProductDetails from '../main/Products/ProductDetails.vue';
import CategoryList from '../main/Products/CategoryList.vue';
import AddCategory from '../main/Products/AddCategory.vue';
import EditCategory from '../main/Products/EditCategory.vue';
import SubcategoryList from '../main/Products/SubcategoryList.vue';
import AddSubcategory from '../main/Products/AddSubcategory.vue';
import EditsubCategory from '../main/Products/EditsubCategory.vue';
import BrandList from '../main/Products/BrandList.vue';
import AddBrand from '../main/Products/AddBrand.vue';
import EditBrand from '../main/Products/EditBrand.vue';
import ImportProduct from '../main/Products/ImportProduct.vue';
import BarCode from '../main/Products/BarCode.vue';
import SalesList from '../main/Sales/SalesList.vue';
import PointofSale from '../main/Sales/PointofSale.vue';
import SalesreturnList from '../main/Sales/SalesreturnList.vue';
import NewsalesreturnList from '../main/Sales/NewsalesreturnList.vue';
import PurchaseList from '../main/Purchases/PurchaseList.vue';
import AddPurchase from '../main/Purchases/AddPurchase.vue';
import ImportPurchase from '../main/Purchases/ImportPurchase.vue';
import ExpenseList from '../main/Expenses/ExpenseList.vue';
import CreateExpense from '../main/Expenses/CreateExpense.vue';
import ExpensecategoryList from '../main/Expenses/ExpensecategoryList.vue';
import AddexpenseCategory from '../main/Expenses/AddexpenseCategory.vue';
import QuotationList from '../main/Quotations/QuotationsList.vue';
import AddQuotation from '../main/Quotations/AddQuotation.vue';
import AddTransfer from '../main/Transfers/AddTransfer.vue';
import TransferList from '../main/Transfers/TransferList.vue';
import ImportTransfer from '../main/Transfers/ImportTransfer.vue';
import PurchasereturnList from '../main/Purchases/PurchasereturnList.vue';
import NewpurchasereturnList from '../main/Purchases/AddpurchaseReturn.vue';
import CustomerList from '../main/People/CustomerList.vue';
import StoreList from '../main/People/StoreList.vue';
import SupplierList from '../main/People/SupplierList.vue';
import UserList from '../main/People/UserList.vue';
import CustomerAdd from '../main/People/CustomerAdd.vue';
import StoreAdd from '../main/People/StoreAdd.vue';
import SupplierAdd from '../main/People/SupplierAdd.vue';
import UserAdd from '../main/People/UserAdd.vue';
import PurchaseOrderReport from '../main/Reports/PurchaseOrderReport.vue';
import InventoryReport from '../main/Reports/InventoryReport.vue';
import SalesReport from '../main/Reports/SalesReport.vue';
import InvoiceReport from '../main/Reports/InvoiceReport.vue';
import PurchaseReport from '../main/Reports/PurchaseReport.vue';
import SupplierReport from '../main/Reports/SupplierReport.vue';
import CustomerReport from '../main/Reports/CustomerReport.vue';
import GeneralSettings from '../main/Settings/GeneralSettings.vue';
import EmailSettings from '../main/Settings/EmailSettings.vue';
import PaymentSettings from '../main/Settings/PaymentSettings.vue';
import CurrencySettings from '../main/Settings/CurrencySettings.vue';
import GroupPermissions from '../main/Settings/GroupPermissions.vue';
import TaxRates from '../main/Settings/TaxRates.vue';
import EditPermissions from '../main/Settings/EditPermission.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            redirect: "/signin",
        },
        {
            path: "/signin",
            name: "SignIn",
            component: SignIn,
        },
        {
            path: "/index",
            name: "Index",
            component: IndexPage,
            children: [
                {
                    path: "dashboard",
                    name: "Dashboard",
                    component: DashboardPage,
                },
                {
                    path: "productlist",
                    name: "ProductList",
                    component: ProductList,
                },
                {
                    path: "addproduct",
                    name: "AddProduct",
                    component: AddProduct,
                },
                {
                    path: "editproduct",
                    name: "EditProduct",
                    component: EditProduct,
                },
                {
                    path: "productdetails",
                    name: "ProductDetails",
                    component: ProductDetails,
                },
                {
                    path: "categorylist",
                    name: "CategoryList",
                    component: CategoryList,
                },
                {
                    path: "addcategory",
                    name: "AddCategory",
                    component: AddCategory,
                },
                {
                    path: "editcategory",
                    name: "EditCategory",
                    component: EditCategory,
                },
                {
                    path: "subcategorylist",
                    name: "SubcategoryList",
                    component: SubcategoryList,
                },
                {
                    path: "addsubcategory",
                    name: "AddSubcategory",
                    component: AddSubcategory,
                },
                {
                    path: "editsubcategory",
                    name: "EditsubCategory",
                    component: EditsubCategory,
                },
                {
                    path: "brandlist",
                    name: "BrandList",
                    component: BrandList,
                },
                {
                    path: "addbrand",
                    name: "AddBrand",
                    component: AddBrand,
                },
                {
                    path: "editbrand",
                    name: "EditBrand",
                    component: EditBrand,
                },
                {
                    path: "importproduct",
                    name: "ImportProduct",
                    component: ImportProduct,
                },
                {
                    path: "printbarcode",
                    name: "BarCode",
                    component: BarCode,
                },
                {
                    path: "saleslist",
                    name: "SalesList",
                    component: SalesList,
                },
                {
                    path: "salesreturnlist",
                    name: "SalesreturnList",
                    component: SalesreturnList,
                },
                {
                    path: "newsalesreturnlist",
                    name: "NewsalesreturnList",
                    component: NewsalesreturnList,
                },
                {
                    path: "purchaselist",
                    name: "PurchaseList",
                    component: PurchaseList,
                },
                {
                    path: "addpurchase",
                    name: "AddPurchase",
                    component: AddPurchase,
                },
                {
                    path: "importpurchase",
                    name: "ImportPurchase",
                    component: ImportPurchase,
                },
                {
                    path: "expenselist",
                    name: "ExpenseList",
                    component: ExpenseList,
                },
                {
                    path: "createexpense",
                    name: "CreateExpense",
                    component: CreateExpense,
                },
                {
                    path: "expensecategorylist",
                    name: "ExpensecategoryList",
                    component: ExpensecategoryList,
                },
                {
                    path: "addexpensecategory",
                    name: "AddExpenseCategory",
                    component: AddexpenseCategory,
                },
                {
                    path: "quotationlist",
                    name: "QuotationList",
                    component: QuotationList,
                },
                {
                    path: "addquotation",
                    name: "AddQuotation",
                    component: AddQuotation,
                },
                {
                    path: "transferlist",
                    name: "TransferList",
                    component: TransferList,
                },
                {
                    path: "addtransfer",
                    name: "AddTransfer",
                    component: AddTransfer,
                },
                {
                    path: "importtransfer",
                    name: "ImportTransfer",
                    component: ImportTransfer,
                },
                {
                    path: "purchasereturnlist",
                    name: "PurchasereturnList",
                    component: PurchasereturnList,
                },
                {
                    path: "newpurchasereturnlist",
                    name: "NewpurchasereturnList",
                    component: NewpurchasereturnList,
                },
                {
                    path: "customerlist",
                    name: "CustomerList",
                    component: CustomerList,
                },
                {
                    path: "storelist",
                    name: "StoreList",
                    component: StoreList,
                },
                {
                    path: "supplierlist",
                    name: "SupplierList",
                    component: SupplierList,
                },
                {
                    path: "userlist",
                    name: "UserList",
                    component: UserList,
                },
                {
                    path: "customeradd",
                    name: "CustomerAdd",
                    component: CustomerAdd,
                },
                {
                    path: "storeadd",
                    name: "StoreAdd",
                    component: StoreAdd,
                },
                {
                    path: "supplieradd",
                    name: "SupplierAdd",
                    component: SupplierAdd,
                },
                {
                    path: "useradd",
                    name: "UserAdd",
                    component: UserAdd,
                },
                {
                    path: "purchaseorderreport",
                    name: "PurchaseOrderReport",
                    component: PurchaseOrderReport,
                },
                {
                    path: "inventoryreport",
                    name: "InventoryReport",
                    component: InventoryReport,
                },
                {
                    path: "salesreport",
                    name: "SalesReport",
                    component: SalesReport,
                },
                {
                    path: "invoicereport",
                    name: "InvoiceReport",
                    component: InvoiceReport,
                },
                {
                    path: "purchasereport",
                    name: "PurchaseReport",
                    component: PurchaseReport,
                },
                {
                    path: "supplierreport",
                    name: "SupplierReport",
                    component: SupplierReport,
                },
                {
                    path: "customerreport",
                    name: "CustomerReport",
                    component: CustomerReport,
                },
                {
                    path: "generalsettings",
                    name: "GeneralSettings",
                    component: GeneralSettings,
                },
                {
                    path: "emailsettings",
                    name: "EmailSettings",
                    component: EmailSettings,
                },
                {
                    path: "paymentsettings",
                    name: "PaymentSettings",
                    component: PaymentSettings,
                },
                {
                    path: "currencysettings",
                    name: "CurrencySettings",
                    component: CurrencySettings,
                },
                {
                    path: "grouppermissions",
                    name: "GroupPermissions",
                    component: GroupPermissions,
                },
                {
                    path: "taxrates",
                    name: "TaxRates",
                    component: TaxRates,
                },
                {
                    path: "editpermission",
                    name: "EditPermission",
                    component: EditPermissions,
                }
                                
            ],
        },
        {
            path: "/pos",
            name: "PointofSale",
            component: PointofSale,
        },
    ],
});

export default router;
