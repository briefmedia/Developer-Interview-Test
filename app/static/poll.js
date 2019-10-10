new Vue({
  el: '#poll',
  data: {
    id: 'e3a98444-eb5a-11e9-81b4-2a2ae2dbcce4',
    active_poll: false,
    selection: false,
    voted: false
  },
  created: function() {
    fetch(`/api/poll/${this.id}`)
    .then((resp) => resp.json())
    .then((response) => {
        this.active_poll = response.data
    })
  },
  methods: {
    vote: function() {
      this.voted = true
      fetch(`/api/vote/${this.id}`, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({'option': ''})
      })
      .then((resp) => resp.json())
      .then((response) => {
          // console.log(response.status)
      })

      console.log('VOTE', this.selection)
    }
  }

})
