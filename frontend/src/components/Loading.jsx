import './Loading.css'

import CircleIcon from '@mui/icons-material/Circle';

function LoadingAnimation() {
    return (
        <div className='loading-animation'>
            <CircleIcon className='loading-dot loading-dot-1' />
            <CircleIcon className='loading-dot loading-dot-2' />
            <CircleIcon className='loading-dot loading-dot-3' />
        </div>
    )
}

export default LoadingAnimation