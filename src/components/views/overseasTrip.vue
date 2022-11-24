<template>
  <swiper ref="filterSwiper" :options="swiperOption" role="tablist">
    <swiper-slide role="tab">111111</swiper-slide>
    <swiper-slide role="tab">222222</swiper-slide>
    <swiper-slide role="tab">333333</swiper-slide>
    <swiper-slide role="tab">444444</swiper-slide>
    <swiper-slide role="tab">555555</swiper-slide>
    <swiper-slide role="tab">666666</swiper-slide>
    <swiper-slide role="tab">777777</swiper-slide>
    <swiper-slide role="tab">888888</swiper-slide>
    <swiper-slide role="tab">999999</swiper-slide>
    <swiper-slide role="tab">101010101010</swiper-slide>
    <swiper-slide role="tab">111111111111</swiper-slide>
    <swiper-slide role="tab">121212121212</swiper-slide>
  </swiper>
</template>
<script>
export default {
	//...
	data () {
      const _vm = this
      return {
        swiperOption: {
           //...
           on: {
             // ...
             resize: function () {
               this.allowTouchMove = !_vm.isOverview
             }
           }
         }
       }
    },
    computed: {
      swiper: function () {
        return this.$refs.filterSwiper.swiper
      },
      isOverview: function () { // swiper 전체 사이즈가 화면을 넘어가는지 여부 확인
        return window.innerWidth >= this.swiper.virtualSize
      }
    },
    methods: {
      swiperInit: function () {
        this.swiper.allowTouchMove = !this.isOverview // 초기 설정에 swiper 사이즈가 화면을 넘어가는지 여부 체크
        this.activeTab()
      }
	},
	mounted () {
     this.swiperInit()
    }
}
</script>
<script>
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import 'C:/git/study_fo/src/assets/css/swiper.min.css'

export default {
  name: 'FilterSwiper',
  data () {
    const _vm = this
    return {
      swiperOption: {
        slidesPerView: 'auto',
        spaceBetween: 6,
        slidesOffsetBefore: 0,
        slidesOffsetAfter: 0,
        freeMode: true,
        centerInsufficientSlides: true,
        on: {
          click: function () {
            _vm.slideMoveTo()	
            _vm.activeTab()						
          },
          tap: function () {
            _vm.slideMoveTo()	
            _vm.activeTab()
          },
          resize: function () {
            this.allowTouchMove = !_vm.isOverview
          }
        }
      }
    }
  },
  methods: {
    swiperInit: function () {
       this.swiper.allowTouchMove = !this.isOverview
       this.activeTab()
    },
    activeTab: function (swiper) {
      swiper = swiper || this.swiper
      if (swiper.hasOwnProperty('clickedSlide') && !swiper.clickedSlide) return

      const slideSelector = `.${swiper.params.slideClass}`
      const selectedEl = swiper.clickedSlide || swiper.slides[swiper.params.initialSlide]
      const swiperArr = document.querySelectorAll(slideSelector)
      Array.from(swiperArr).forEach((el) => {
        el.setAttribute('aria-selected', 'false')
        selectedEl.setAttribute('aria-selected', 'true')
      })
    },
    slideMoveTo: function (swiper = this.swiper) {
      if (!swiper.clickedSlide) return

      const activeIndex = swiper.clickedIndex
      swiper.slideTo(activeIndex)
    }
  },
  computed: {
    swiper: function () {
      return this.$refs.filterSwiper.swiper
    },
    isOverview: function () {
      return window.innerWidth >= this.swiper.virtualSize
    }
  },
  mounted () {
    this.swiperInit()
  },
  components: {
    swiper,
    swiperSlide
  }
}
</script>
<style lang="scss" scoped>
.swiper-container {
  padding: 0 20px;
  &:before,
  &:after {
    display: block;
    position: absolute;
    top: 0;
    width: 20px;
    height: 100%;
    z-index: 10;
    content: "";
  }
  &:before {
    left: 0;
    background: linear-gradient(90deg, #fff -20.19%, rgba(255, 255, 255, 0.8) 18.31%, rgba(255, 255, 255, 0) 75%);
  }
  &:after {
    right: 0;
    background: linear-gradient(270deg, #fff -20.19%, rgba(255, 255, 255, 0.8) 18.31%, rgba(255, 255, 255, 0) 75%);
  }
  .swiper-wrapper {
    .swiper-slide {
      width: auto;
      min-width: 56px;
      padding: 0px 14px;
      font-size: 14px;
      line-height: 36px;
      text-align: center;
      color: #84868c;
      border: 0;
      border-radius: 18px;
      background: #f3f4f7;
      appearance: none;
      cursor: pointer;
      &[aria-selected="true"] {
        color: #fff;
        background: #000;
      }
    }
  }
}
</style>