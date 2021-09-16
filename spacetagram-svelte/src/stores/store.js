import {persistStore} from './persistStore'

const defaultData = []

export const store = persistStore('likedImages', defaultData)