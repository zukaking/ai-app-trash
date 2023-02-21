<template>
  <div>
    <video ref="video" id="video" width="500" height="500" autoplay></video>
    <div>
      <button color="info" id="snap" v-on:click="capture()">Snap Photo</button>
    </div>
    <canvas ref="canvas" id="canvas" width="500" height="500"></canvas>
  </div>
</template>


<script>

const rootname = "http://ec2-3-112-7-45.ap-northeast-1.compute.amazonaws.com"

import axios from 'axios'
import {reactive} from 'vue'

const smRequests = reactive({
  Image: ''
})


export default {
  name: 'CameraSet',
  data(){
    return {
      showOutput: false,
      smRetvalue:'unkown'
    }
  },
  mounted () {
    this.video = this.$refs.video
    console.log(navigator.mediaDevices)
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      console.log('true')
      navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
        this.video.srcObject = stream
        this.video.play()
      })
    }
  },
  methods: {
    capture () {
      this.canvas = this.$refs.canvas

      const endPoint = rootname + ':5000/api/sm'
      this.canvas.getContext('2d').drawImage(this.video, 0, 0, 500, 500)
      smRequests.Image = this.canvas.toDataURL('image/png')
      axios.post(endPoint,smRequests).then(
        (response) => {
          this.smRetvalue = response.data.result
          this.showOutput = true
        }
      ).catch( (error) => {
        console.log(error)
      })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
