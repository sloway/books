import {
  SET_MESSAGES,
  GET_CHANNELS
} from './mutation-types'

export default {
  [GET_CHANNELS](state, channels) {
    state.channels = channels
  },
  [SET_MESSAGES](state, messages) {
    state.messages = messages
  }
}

