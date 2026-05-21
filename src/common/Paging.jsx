import { useCallback, useEffect, useState } from 'react';
import { Container, Sprite, Text } from '@pixi/react';
import * as AssetsFactory from '@common/AssetsFactory';
import '@pixi/events';

// Paging component for list display, with page navigation buttons and page number display
export const Paging = (props) => {
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json");

    const [currentPage, setCurrentPage] = useState(1);
    // item shows for each page, default is 10
    const pageItemSize = props.pageItemSize || 10;
    const totalPage = Math.ceil(props.dataList.length / pageItemSize);

    // page number to display, max is 5
    const visiblePageCount = Math.min(5, totalPage);
    const maxStartPage = Math.max(1, totalPage - visiblePageCount + 1);
    const startPage = Math.max(1, Math.min(currentPage - 2, maxStartPage));
    const pageNumberList = Array.from({ length: visiblePageCount }, (_, i) => startPage + i);

    return (
        <Container x={props.x} y={props.y}>
            {/* go to first page */}
            <Sprite texture={commonMain[7]} x={0} y={0} interactive
                pointerup={() => {
                    setCurrentPage(1);
                    props.setCurrentPageList(props.dataList.slice(0, pageItemSize))
                }
                } />
            {/* go to previous page */}
            <Sprite texture={commonMain[9]} x={60} y={0} interactive
                pointerup={() => {
                    setCurrentPage(Math.max(1, currentPage - 1));
                    if (currentPage > 1) {
                        props.setCurrentPageList(props.dataList.slice((currentPage - 2) * pageItemSize, (currentPage - 1) * pageItemSize));
                    }
                }
                } />
            {pageNumberList.map(
                (i, index) => <Text
                    key={i}
                    interactive
                    buttonMode
                    pointerup={() => { setCurrentPage(i); props.setCurrentPageList(props.dataList.slice((i - 1) * pageItemSize, i * pageItemSize)); }}
                    text={`${i}`}
                    x={index * 50 + 140}
                    y={12}
                    anchor={{ x: 0.5, y: 0.5 }}
                    style={currentPage === i ? { fill: '0x22a39f', fontSize: 30 } : { fill: 'black', fontSize: 26 }}
                />
            )}
            {/* go to next page */}
            <Sprite texture={commonMain[8]} x={380} y={0} interactive
                pointerup={
                    () => {
                        setCurrentPage(Math.min(totalPage, currentPage + 1));
                        if (currentPage < totalPage) {
                            props.setCurrentPageList(props.dataList.slice((currentPage) * pageItemSize, (currentPage + 1) * pageItemSize));
                        }
                    }
                } />
            {/* go to last page */}
            <Sprite texture={commonMain[6]} x={430} y={0} interactive
                pointerup={() => {
                    setCurrentPage(totalPage);
                    props.setCurrentPageList(props.dataList.slice((totalPage - 1) * pageItemSize, totalPage * pageItemSize));
                }} />
        </Container>
    );

};