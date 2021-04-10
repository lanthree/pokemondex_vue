<template>
  <div class="logo-wrapper">
    <span class="left-1" :style="L1StyleObject" />
    <span class="left-2" :style="L2StyleObject" />
    <span class="logo-img-wrapper">
      <img
        class="logo-img"
        v-bind:src="require('../assets/logo/' + typeName + '.png')"
      />
    </span>
    <span class="type-name">{{ typeName }}</span>
  </div>
</template>

<script>
export default {
  name: "TypeLogo",
  props: {
    typeName: {
      type: String,
      default: "普通",
    },
  },
  data() {
    var logoColor = this.GetColorByTypeName();

    return {
      L1StyleObject: {
        backgroundColor: logoColor,
      },
      L2StyleObject: {
        borderColor: logoColor,
        borderRightColor: "#00000000",
        borderBottomColor: "#00000000",
      },
    };
  },
  methods: {
    GetColorByTypeName() {
      switch (this.typeName) {
        case "一般":
          return "#9199A1";
        case "格斗":
          return "#CD406A";
        case "飞行":
          return "#8EA8DE";
        case "毒":
          return "#A96AC8";
        case "地面":
          return "#D87844";
        case "岩石":
          return "#C5B78B";
        case "虫":
          return "#91C12E";
        case "幽灵":
          return "#5369AC";
        case "钢":
          return "#5A8DA1";
        case "火":
          return "#FE927D";
        case "水":
          return "#4f90d5";
        case "草":
          return "#62BB5A";
        case "电":
          return "#F3D23B";
        case "超能力":
          return "#F87178";
        case "冰":
          return "#73CEBF";
        case "龙":
          return "#0D6DC2";
        case "恶":
          return "#5A5265";
        case "妖精":
          return "#EB8FE6";
        default:
          return "#9199A1";
      }
    },
  },
};
</script>

<style scoped>
.logo-wrapper {
  background-color: #5f4f44;
  color: white;
  font-size: 13px;
  padding-left: 20px;
  width: 40px;
  height: 20px;
  border-radius: 6px;
  vertical-align: middle;
  text-align: center;
  position: relative;
  overflow: hidden;
  display: inline-block;
  margin: 0 2px 0 2px;
}
.left-1 {
  position: absolute;
  top: 0;
  left: 0;
  width: 17px;
  height: 20px;
}
.left-2 {
  position: absolute;
  top: 0;
  left: 17px;
  border-width: 10px 3px;
  border-style: solid;
}
.logo-img-wrapper {
  position: absolute;
  top: -1;
  left: 0;
}
.logo-img {
  width: 20px;
  height: 20px;
}
.type-name {
  line-height: 20px;
  text-align: center;
}
</style>