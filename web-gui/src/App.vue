<script>

  export default {
    data() {
      return {

        /** TODO machines will be populated with cluster elements id*/
        machines: [1,2,3],

        machine: null,
        machine_data: {},
        onMachineSelected: () => {

          console.log('Selected: ', this.machine);
          
          /**
           *  TODO change address based on selected machine value
           * ie.: http://machine.1:8082/v1/water
           */
          fetch("http://localhost:8082/v1/water")
            .then(response => response.json())
            .then(data => {
              console.log(data)
              this.machine_data.water = data.response.water
            });

        }
      }
    },

    mounted() {
    }

  }

</script>

<template>
  <header>
    <img alt="Hy logo" class="logo" src="./assets/plant.png" width="125" height="125" />

    <div class="wrapper">
      <h1 class="green">{{ "Hydroponic system" }}</h1>
    </div>
  </header>

  <main>

    <div>Machine Number</div>

    <select v-model="machine" @change="onMachineSelected()">
      <option disabled value="">Please select one</option>
      <option v-for="machine_id in machines" :value="machine_id">
        {{ machine_id }}
      </option>
    </select>

    <div class="machine" v-if=machine_data.water>Water: {{ machine_data.water }}</div>

  </main>
</template>

<style>
@import './assets/base.css';

#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;

  font-weight: normal;
}

h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

.machine {
  margin-top: 20px;
}

a,
.green {
  text-decoration: none;
  color: hsla(160, 100%, 37%, 1);
  transition: 0.4s;
}

@media (hover: hover) {
  a:hover {
    background-color: hsla(160, 100%, 37%, 0.2);
  }
}

@media (min-width: 1024px) {
  body {
    display: flex;
    place-items: center;
  }

  #app {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 0 2rem;
  }

  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  .logo {
    margin: 0 2rem 0 0;
  }
}
</style>
