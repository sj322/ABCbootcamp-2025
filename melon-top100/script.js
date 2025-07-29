

const chartCtx = document.getElementById('melonChart').getContext('2d');
const loadingMsg = document.getElementById('loadingMessage');

// 날짜별 JSON URL (확장 가능)
const chartDates = [
    '20231204',
    // 필요시 추가: '20231211', '20231218', ...
];
const jsonBaseUrl = 'https://pyhub.kr/melon/';

async function fetchChartData() {
    const allData = [];
    for (const date of chartDates) {
        try {
            const res = await fetch(jsonBaseUrl + date + '.json');
            if (!res.ok) throw new Error('데이터 조회 실패: ' + date);
            const data = await res.json();
            allData.push({ date, data });
        } catch (e) {
            loadingMsg.textContent = e.message;
            throw e;
        }
    }
    return allData;
}

function processTop10Rankings(allData) {
    // 곡별로 {title, artist, ranks: [rank, ...]} 형태로 변환
    const songMap = new Map();
    allData.forEach(({ date, data }, idx) => {
        data.slice(0, 10).forEach((song, rankIdx) => {
            const key = song.title + ' - ' + song.artist;
            if (!songMap.has(key)) {
                songMap.set(key, { title: song.title, artist: song.artist, ranks: Array(allData.length).fill(null) });
            }
            songMap.get(key).ranks[idx] = rankIdx + 1; // 1위부터 10위까지
        });
    });
    return Array.from(songMap.values());
}

function makeLineChart(labels, songs) {
    const colors = [
        '#4CAF50', '#FF6384', '#36A2EB', '#FFCE56', '#8E44AD', '#E67E22', '#2ECC71', '#E74C3C', '#3498DB', '#F1C40F'
    ];
    const datasets = songs.map((song, i) => ({
        label: song.title + ' (' + song.artist + ')',
        data: song.ranks,
        borderColor: colors[i % colors.length],
        backgroundColor: colors[i % colors.length] + '33',
        tension: 0.3,
        spanGaps: true,
    }));
    new Chart(chartCtx, {
        type: 'line',
        data: {
            labels,
            datasets
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: true, position: 'bottom' },
                title: { display: false }
            },
            scales: {
                y: {
                    reverse: true, // 1위가 위로
                    min: 1,
                    max: 10,
                    ticks: { stepSize: 1 }
                }
            }
        }
    });
}

(async function main() {
    try {
        const allData = await fetchChartData();
        const labels = allData.map(({ date }) => date.replace(/(\d{4})(\d{2})(\d{2})/, '$1-$2-$3'));
        const songs = processTop10Rankings(allData);
        loadingMsg.style.display = 'none';
        makeLineChart(labels, songs);
    } catch (e) {
        // 에러 메시지는 fetchChartData에서 처리
    }
})();
