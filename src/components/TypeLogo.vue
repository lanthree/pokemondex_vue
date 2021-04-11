<template>
  <div class="logo-wrapper" :style="LWStypeObject">
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
    var logoColor = this.GetLogoColorByTypeName();
    var backColor = this.GetBackColorByTypeName();

    return {
      LWStypeObject: {
        backgroundColor: backColor,
      },
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
    GetLogoColorByTypeName() {
      switch (this.typeName) {
        case "一般":
          return "#909ca2";
        case "格斗":
          return "#ce4267";
        case "飞行":
          return "#90a9dc";
        case "毒":
          return "#a96ac9";
        case "地面":
          return "#d97846";
        case "岩石":
          return "#c6b88a";
        case "虫":
          return "#91c12c";
        case "幽灵":
          return "#526aad";
        case "钢":
          return "#5a8fa3";
        case "火":
          return "#ff9d54";
        case "水":
          return "#4e92d2";
        case "草":
          return "#63bc5a";
        case "电":
          return "#f4d43b";
        case "超能力":
          return "#fb717b";
        case "冰":
          return "#73d0bd";
        case "龙":
          return "#0c6cc4";
        case "恶":
          return "#5a5467";
        case "妖精":
          return "#ed91e3";
        default:
          return "#9199A1";
      }
    },
    GetBackColorByTypeName() {
      switch (this.typeName) {
        case "一般":
          return "#4c504f";
        case "格斗":
          return "#594149";
        case "飞行":
          return "#4d515a";
        case "毒":
          return "#524858";
        case "地面":
          return "#5b4940";
        case "岩石":
          return "#58554e";
        case "虫":
          return "#4d553e";
        case "幽灵":
          return "#424953";
        case "钢":
          return "#444d52";
        case "火":
          return "#605043";
        case "水":
          return "#424e5a";
        case "草":
          return "#445547";
        case "电":
          return "#5d5a42";
        case "超能力":
          return "#5e484a";
        case "冰":
          return "#465858";
        case "龙":
          return "#374957";
        case "恶":
          return "#44454a";
        case "妖精":
          return "#5c4e5d";
        default:
          return "#4c504f";
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
  padding-left: 25px;
  width: 40px;
  height: 20px;
  border-radius: 1px;
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
  width: 22px;
  height: 20px;
}
.left-2 {
  position: absolute;
  top: 0;
  left: 21px;
  border-width: 11px 4px;
  border-style: solid;
}
.logo-img-wrapper {
  position: absolute;
  top: 1px;
  left: 3px;
  text-align: center;
}
.logo-img {
  width: 18px;
  height: 18px;
}
.type-name {
  line-height: 20px;
  text-align: center;
}
</style>