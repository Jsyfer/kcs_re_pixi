import { create } from "zustand"

// 使用共通存储池
export const useStore = create((set) => ({
  portData: null, // 母港数据
  setPortData: (value) => set({ portData: value }),
  getData: null, //基础数据
  setGetData: (value) => set({ getData: value }),
  requireInfo: null, //必要数据
  setRequireInfo: (value) => set({ requireInfo: value }),
}))
