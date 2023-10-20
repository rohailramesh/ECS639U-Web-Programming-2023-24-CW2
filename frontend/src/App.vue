<template>
  <div class="container pt-3">
    <div class="h1 text-center border rounded bg-light p-2 mb-3">
      API Client
    </div>
    <div class="mb-3"><u>Response data</u>:</div>
    <GetClaimInfo />
  </div>
</template>

<script>
import GetClaimInfo from "./components/GetClaimInfo.vue";

export default {
  components: {
    GetClaimInfo,
  },
};
</script>
