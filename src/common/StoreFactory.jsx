import { create } from "zustand"

export const useStore = create((set) => ({
  portData: null,
  setPortData: (value) => set({ portData: value }),
  getData: null,
  setGetData: (value) => set({ getData: value }),
  requireInfo: null,
  setRequireInfo: (value) => set({ requireInfo: value }),
}))
