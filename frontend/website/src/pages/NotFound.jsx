import './NotFound.css'

import ErrorOutlineIcon from '@mui/icons-material/ErrorOutline';

function NotFound() {
    return (
        <div id='NotFound'>
            <h1>Uh Oh!</h1>
            <h2>We Can't Find This!</h2>
            <ErrorOutlineIcon id='icon-404' />
        </div>
    )
}

export default NotFound