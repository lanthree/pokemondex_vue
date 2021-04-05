<template>
  <v-chart class="chart" :option="option" />
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { RadarChart } from "echarts/charts";
import VChart from "vue-echarts";

use([CanvasRenderer, RadarChart]);

export default {
  name: "SpeciesStrengthRadar",
  components: {
    VChart,
  },
  props: {
    ss: {
      type: Array,
      default: () => [100, 100, 100, 100, 100, 100],
    },
  },
  data() {
    return {
      option: {
        radar: {
          indicator: [
            {
              name: "HP\n" + this.ss[0],
              max: 252,
            },
            {
              name: "特攻\n" + this.ss[1],
              max: 252,
            },
            {
              name: this.ss[2] + "\n特防",
              max: 252,
            },
            {
              name: this.ss[3] + "\n速度",
              max: 252,
            },
            {
              name: this.ss[4] + "\n防御",
              max: 252,
            },
            {
              name: "攻击\n" + this.ss[5],
              max: 252,
            },
          ],
          shape: "polygon",
          splitNumber: 0,
          axisName: {
            color: "#000",
            fontWeight: "bold",
            fontFamily: "monospace",
            fontSize: 12,
            lineHeight: 13,
          },
          splitArea: {
            areaStyle: {
              color: ["#DDDDDD"],
            },
          },
          axisLine: {
            lineStyle: {
              color: "#FFF",
              width: 1.4,
            },
          },
        },
        series: [
          {
            type: "radar",
            lineStyle: {
              width: 1,
              opacity: 0.8,
            },
            data: [this.ss],
            symbol: "none",
            itemStyle: {
              color: "#A595F9",
            },
            areaStyle: {
              opacity: 0.8,
            },
          },
        ],
      },
    };
  },
};
</script>

<style scoped>
.chart {
  width: 250;
  height: 270px;
}
</style>