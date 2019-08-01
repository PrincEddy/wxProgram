Page({
  data: {
    PageCur: 'wechat'
  },
  options: {
    addGlobalClass: true,
  },
  NavChange(e) {
    this.setData({
      PageCur: e.currentTarget.dataset.cur
    })
  },
  onShareAppMessage() {
    return {
      title: '等车咯',
      imageUrl: '/images/share.jpg',
      path: '/pages/index/index'
    }
  },
})