<template>
  <div class="section">
    <div class="container">
      <h1 class="title">CO2 Emission Table by Carriers</h1>
      <p>
        *All values are relative to the selected period of time. The default start time is
        October 2020.
      </p>
      <div class="content">
        <table class="table is-hoverable">
          <thead>
            <tr>
              <th
                class="clickable-title"
                @click="sort('carrier_company_id')">
                Carrier Name
                <font-awesome-icon icon="arrows-alt-v"/>
              </th>
              <th
                class="clickable-title"
                @click="sort('total_co2_emitted__sum')">
                Total CO2 Emission
                 <font-awesome-icon icon="arrows-alt-v"/>
              </th>
              <th
                class="clickable-title"
                @click="sort('travelled_distance__sum')">
                Total Distance
                 <font-awesome-icon icon="arrows-alt-v"/>
              </th>
              <th
                class="clickable-title"
                @click="sort('weight__avg')">
                Average weight of shipments
                <font-awesome-icon icon="arrows-alt-v"/>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="carrier in carriersData" :key="carrier.carrier_company_id">
              <td>{{carrier.carrier_company_id}}</td>
              <td>{{carrier.total_co2_emitted__sum | roundUp}}</td>
              <td>{{carrier.travelled_distance__sum | roundUp}}</td>
              <td>{{carrier.weight__avg | roundUp}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CO2AnalyticsTable',
  data() {
    return {
      carriersData: [],
      sortDir: 'asc',
    };
  },
  mounted() {
    this.fetchAnalyticsData();
  },
  methods: {
    async fetchAnalyticsData() {
      try {
        const { data } = await axios.get('http://localhost:8000/api/carriers/all');
        this.carriersData = data;
      } catch (error) {
        console.log(error);
      }
    },
    sort(fieldName) {
      this.sortDir = this.sortDir === 'asc' ? 'desc' : 'asc';
      let modifierOne = -1;
      let modifierTwo = 1;
      if (this.sortDir === 'desc') {
        modifierOne = 1;
        modifierTwo = -1;
      }
      this.carriersData.sort((a, b) => {
        if (a[fieldName] < b[fieldName]) {
          return modifierOne;
        }
        if (a[fieldName] > b[fieldName]) {
          return modifierTwo;
        }
        return 0;
      });
    },
  },
};
</script>

<style scoped>
.clickable-title{
  cursor: pointer
}
</style>
