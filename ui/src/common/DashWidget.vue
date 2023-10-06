<template>
  <div class="dash-widget dash2">
    <div class="dash-widgetimg">
      <span><img src="/img/icons/dash3.svg" alt="img" /></span>
    </div>
    <div class="dash-widgetcontent">
      <h5>
        ₱<span class="counters" :data-count="totalPurchaseAmount">{{
          totalPurchaseAmount
        }}</span>
      </h5>
      <h6>Total Sales Amount</h6>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    initialtotalPurchaseAmount: {
      type: Number,
      default: 10,
    },
  },
  data() {
    return {
      totalPurchaseAmount: this.initialtotalPurchaseAmount,
    };
  },
};
</script>
<style></style>
