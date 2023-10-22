<template>
  <div class="container pt-3">
    <div class="h1 text-center border rounded bg-light p-2 mb-3">
      API Client
    </div>
    <div class="mb-3"><u>Response data</u>:</div>
    <GetClaimInfo @claim-info="handleClaimInfo" />
    <div v-if="receivedClaimInfo">
      <p>
        <strong>Received Claim Info:</strong>
      </p>
      <p><strong>Module name:</strong>{{ receivedClaimInfo.module_name }}</p>
      <p><strong>Hours worked:</strong>{{ receivedClaimInfo.hours_worked }}</p>
      <p>
        <strong>QM claim for submitted:</strong
        >{{ receivedClaimInfo.claim_form_submitted }}
      </p>
      <p>
        <strong>Demonstrated date:</strong
        >{{ receivedClaimInfo.demonstrated_date }}
      </p>
    </div>
    <br />
    <add-demo-claim-vue />
    <br />
    <delete-claim-vue />
    <br />
    <update-claim-form-vue />
    <br />
    <get-all-claims-vue />
    <br />
  </div>
</template>

<script>
import AddDemoClaimVue from "./components/AddDemoClaim.vue";
import DeleteClaimVue from "./components/DeleteClaim.vue";
import GetAllClaimsVue from "./components/GetAllClaims.vue";
import GetClaimInfo from "./components/GetClaimInfo.vue";
import UpdateClaimFormVue from "./components/UpdateClaimForm.vue";

export default {
  components: {
    GetClaimInfo,
    AddDemoClaimVue,
    DeleteClaimVue,
    UpdateClaimFormVue,
    GetAllClaimsVue,
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
