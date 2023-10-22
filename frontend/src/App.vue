<template>
  <div class="container pt-3">
    <div class="h1 text-center border rounded bg-light p-2 mb-3">
      API Client
    </div>
    <div class="mb-3"><u>Response data</u>:</div>
    <GetClaimInfo @claim-info="handleClaimInfo" />
    <div v-if="receivedClaimInfo">
      <p>
        <strong>Received Claim Info:</strong>{{ receivedClaimInfo.module_name }}
      </p>
    </div>
    <add-demo-claim-vue />
    <delete-claim-vue />
    <update-claim-form-vue />
  </div>
</template>

<script>
import AddDemoClaimVue from "./components/AddDemoClaim.vue";
import DeleteClaimVue from "./components/DeleteClaim.vue";
import GetClaimInfo from "./components/GetClaimInfo.vue";
import UpdateClaimFormVue from "./components/UpdateClaimForm.vue";

export default {
  components: {
    GetClaimInfo,
    AddDemoClaimVue,
    DeleteClaimVue,
    UpdateClaimFormVue,
  },
  data() {
    return {
      receivedClaimInfo: null,
    };
  },
  methods: {
    handleClaimInfo(claimInfo) {
      //This method called when custom method is emiited from child component
      this.receivedClaimInfo = claimInfo;
    },
  },
};
</script>
