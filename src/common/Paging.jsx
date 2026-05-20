import { useCallback, useEffect, useState } from 'react';
import { Container, Sprite, Text } from '@pixi/react';
import { PixiButton } from '@common/PixiButton';
import * as AssetsFactory from '@common/AssetsFactory';
import '@pixi/events';

// 翻页组件
export const Paging = (props) => {
    const [currentPage, setCurrentPage] = useState(1);
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")

    const visibleCount = Math.min(5, props.totalPage);
    const maxStartPage = Math.max(1, props.totalPage - visibleCount + 1);
    const startPage = Math.max(1, Math.min(currentPage - 2, maxStartPage));
    const pageList = Array.from({ length: visibleCount }, (_, i) => startPage + i);

    return (
        <Container x={props.x} y={props.y}>
            {/* go to first page */}
            <PixiButton default={commonMain[7]} x={0} y={0} action={() => setCurrentPage(1)} />
            {/* go to previous page */}
            <PixiButton default={commonMain[9]} x={60} y={0} action={() => setCurrentPage(Math.max(1, currentPage - 1))} />
            {pageList.map(
                (i, index) => <Text
                    key={i}
                    interactive
                    buttonMode
                    pointerdown={() => setCurrentPage(i)}
                    text={`${i}`}
                    x={index * 50 + 140}
                    y={12}
                    anchor={{ x: 0.5, y: 0.5 }}
                    style={currentPage === i ? { fill: '0x22a39f', fontSize: 28 } : { fill: 'black', fontSize: 26 }}
                />
            )}
            {/* go to next page */}
            <PixiButton default={commonMain[8]} x={380} y={0} action={() => setCurrentPage(Math.min(props.totalPage, currentPage + 1))} />
            {/* go to last page */}
            <PixiButton default={commonMain[6]} x={430} y={0} action={() => setCurrentPage(props.totalPage)} />
        </Container>
    );

};