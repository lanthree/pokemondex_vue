<template>
  <div id="app">
    <el-container>
      <el-aside style="width: 230px">
        <div class="search">
          <el-input
            v-if="renderSearcher"
            autofocus="true"
            placeholder="输入关键字进行过滤"
            v-model="filterText"
          >
          </el-input>
        </div>
        <el-scrollbar id="pokedex" :style="{ height: slbHeight }">
          <el-tree
            class="filter-tree"
            :data="data"
            :props="defaultProps"
            default-expand-all
            :filter-node-method="filterNode"
            @node-click="clickNode"
            ref="tree"
            v-if="refreshed"
          >
            <div
              class="custom-tree-node"
              slot-scope="{ node }"
              style="display: flex"
            >
              <img
                v-if="node.data.bid"
                v-bind:src="require('./assets/icons/' + node.data.bid + '.png')"
                style="height: 24px; flex: 0.3"
              />
              <span style="flex: 0.7">
                {{ node.label }}
              </span>
            </div>
          </el-tree>
        </el-scrollbar>
      </el-aside>
      <el-main id="content">
        <el-scrollbar :style="{ height: contentHeight }">
          <Content :bid="bid" :label="selected_label" v-if="selected" />
        </el-scrollbar>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Content from "./components/Content.vue";

export default {
  name: "App",
  data() {
    const { data } = require("./assets/data/indexes.js");
    return {
      bid: "001",
      selected_label: "001 妙蛙種子",
      selected: true,
      //
      filterText: "",
      data: data,
      defaultProps: {
        children: "children",
        label: "label",
      },
      clientHeight: "", //浏览器可视区域高度
      clientWidth: "",
      slbHeight: "",
      contentHeight: "",
      height_timer: false,
      width_timer: false,
      alpha_201_sheet: null,
      refreshed: false,
      renderSearcher: true,
    };
  },
  components: {
    Content,
  },
  methods: {
    filterNode(value, data) {
      this.clearBig();

      if (!value) return true;
      if (data.match === undefined) return false;
      if (data.match.indexOf(value) === -1) return false;

      this.changeBid(data.bid);
      return true;
    },
    clickNode(data) {
      this.clearBig();
      this.changeBid(data.bid);
    },
    changeBid(bid) {
      if (bid === undefined) return;
      if (this.bid !== "") return;

      this.selected = false;
      this.bid = bid;
      this.$nextTick(() => {
        this.selected = true;
      });
    },
    clearBig() {
      if (this.selected === true) this.bid = "";
    },
    changeFixed(clientHeight, clientWidth) {
      if (clientHeight != -1) {
        // 自适应的滚动条高度
        this.slbHeight = clientHeight - 60 + "px";
        if (!this.renderSearcher) {
          this.slbHeight = clientHeight - 20 + "px";
        }
        this.contentHeight = clientHeight - 10 + "px";
      }
      if (clientWidth != -1) {
        // 自适应的未知图腾的字母表table的图片大小
        // 通过后续增加style元素实现
        // -- Q: 为什么不直接get元素？A: mounted时get不到元素 还未渲染到
        if (this.alpha_201_sheet == null) {
          var style = document.createElement("style");
          style.appendChild(document.createTextNode(""));
          document.head.appendChild(style);
          this.alpha_201_sheet = style.sheet;
        } else {
          this.alpha_201_sheet.deleteRule(0);
        }
        var img_width = (clientWidth - 230 - 250 - 120) / 7;
        this.alpha_201_sheet.insertRule(
          "#alpha-201 img{width:" + img_width + "px}"
        );
      }

      this.refreshed = true;
    },
  },
  mounted() {
    if (window.utools) {
      this.renderSearcher = false;
      window.utools.onPluginEnter(() => {
        window.utools.setSubInput(({ text }) => {
          console.log(text);
          this.$refs.tree.filter(text);
        });
      });
    }

    this.changeFixed(
      `${document.documentElement.clientHeight}`,
      `${document.documentElement.clientWidth}`
    );

    const that = this;
    window.onresize = () => {
      return (() => {
        that.clientHeight = `${document.documentElement.clientHeight}`;
        that.clientWidth = `${document.documentElement.clientWidth}`;
      })();
    };
  },
  watch: {
    filterText(val) {
      this.$refs.tree.filter(val);
    },
    clientHeight(val) {
      if (!this.height_timer) {
        //如果clientHeight 发生改变，这个函数就会运行
        this.changeFixed(val, -1);
        this.height_timer = true;
        let _this = this;
        setTimeout(function () {
          _this.height_timer = false;
        }, 100);
      }
    },
    clientWidth(val) {
      if (!this.width_timer) {
        //如果clientWidth 发生改变，这个函数就会运行
        this.changeFixed(-1, val);
        this.width_timer = true;
        let _this = this;
        setTimeout(function () {
          _this.width_timer = false;
        }, 100);
      }
    },
  },
};
</script>

<style>
body {
  margin: 0;
  padding: 0;
  background-color: white;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0px;
  height: 100%;
}
.filter-tree {
  margin-top: 20px;
}
.el-aside {
  margin: 10px;
}
.search {
  margin-left: 10px;
  margin-right: 10px;
}
#content {
  padding: 0;
  margin-top: 5px;
  margin-bottom: 5px;
  margin-right: 10px;
}
</style>
