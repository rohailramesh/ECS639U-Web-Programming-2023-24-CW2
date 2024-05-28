<template>
  <div class="background">
    <nav class="navbar navbar-expand-lg bg-light backgroundNav">
      <div class="container">
        <a class="navbar-brand" href="#"><h1>CLAIM-IT-QM</h1></a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ml-auto buttonsNav">
            <li class="nav-item">
              <button
                type="button"
                class="button"
                data-bs-toggle="modal"
                data-bs-target="#addClaimModal"
              >
                Add Claim
              </button>
            </li>
            <li class="nav-item">
              <button
                type="button"
                class="button"
                data-bs-toggle="modal"
                data-bs-target="#deleteClaimModal"
              >
                Delete Claim
              </button>
            </li>
            <li class="nav-item">
              <button
                type="button"
                class="button"
                data-bs-toggle="modal"
                data-bs-target="#updateClaimModal"
              >
                Update Claim
              </button>
            </li>
            <li class="nav-item">
              <button
                type="button"
                class="button"
                data-bs-toggle="modal"
                data-bs-target="#findClaimModal"
              >
                Find Claim
              </button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div>
      <modal-vue modalId="findClaimModal" modalTitle="Find Claim">
        <GetClaimInfo @claim-info="handleClaimInfo" />
        <div v-if="receivedClaimInfo">
          <div class="container mt-4">
            <h2>Received Claim Info</h2>
            <div class="card">
              <div class="card-body">
                <p class="card-text">
                  <strong>Claim ID:</strong>
                  {{ receivedClaimInfo.ID }}
                </p>
                <p class="card-text">
                  <strong>Module name:</strong>
                  {{ receivedClaimInfo.module_name }}
                </p>
                <p class="card-text">
                  <strong>Hours worked:</strong>
                  {{ receivedClaimInfo.hours_worked }}
                </p>
                <p class="card-text">
                  <strong>QM claim for submitted:</strong>
                  {{ receivedClaimInfo.claim_form_submitted }}
                </p>
                <p class="card-text">
                  <strong>Demonstrated date:</strong>
                  {{ receivedClaimInfo.demonstrated_date }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </modal-vue>
      <br />
      <div class="container pt-3">
        <modal-vue modalId="addClaimModal" modalTitle="Add New Claim">
          <add-demo-claim-vue />
        </modal-vue>
        <modal-vue modalId="deleteClaimModal" modalTitle="Delete Claim">
          <delete-claim-vue />
        </modal-vue>
        <modal-vue modalId="updateClaimModal" modalTitle="Update Claim">
          <update-claim-form-vue />
        </modal-vue>
        <get-all-claims-vue />
      </div>
    </div>
  </div>
</template>
<script>
import AddDemoClaimVue from "./components/AddDemoClaim.vue";
import DeleteClaimVue from "./components/DeleteClaim.vue";
import GetAllClaimsVue from "./components/GetAllClaims.vue";
import GetClaimInfo from "./components/GetClaimInfo.vue";
import ModalVue from "./components/Modal.vue";
import UpdateClaimFormVue from "./components/UpdateClaimForm.vue";

export default {
  components: {
    GetClaimInfo,
    AddDemoClaimVue,
    DeleteClaimVue,
    UpdateClaimFormVue,
    GetAllClaimsVue,
    ModalVue,
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
<style>
.navButton {
  margin-right: 10px;
  margin-bottom: 10px;
}
* {
  font-family: "Times New Roman", Times, serif;
}
.buttonsNav {
  margin-left: 200px;
  align-content: center;
  justify-content: center;
  text-align: center;
}
.name {
  font-size: 30px;
}
.background {
  /* Use the URL of your image here */
  background-image: url("/Users/rohailramesh/Downloads/ECS639U-Web-Programming-2023-24-CW2-046dd42116e4e19741c6dcbfa880d97b1a79caa4/frontend/src/images/background.jpg");

  /* Full viewport height */
  height: 100vh;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative; /* Add this line to make sure the content is positioned correctly on top of the background */
}
.backgroundNav {
  background-color: #ececee;
}
.button {
  background-color: #a79d88;
  border-radius: 10px;
  border-width: 0;
  display: inline-block;
  font-weight: 400;
  text-align: center;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  color: #fff;
  margin-right: 10px;
}
</style>
