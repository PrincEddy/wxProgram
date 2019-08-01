const app = getApp();
Component({
  options: {
    addGlobalClass: true,
  },
  data: {
    CustomBar: app.globalData.CustomBar,
  },
  methods: {
    searchIcon(e) {
      wx.request({
        url: 'http://bus.wuhancloud.cn:9087/website//web/420100/search.do?keyword=576&type=line',
        method: "POST",
        success(res) {
          console.log(res)
        },
      });
    },
  },

})