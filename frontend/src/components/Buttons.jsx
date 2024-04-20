import './Buttons.css'

function PrimaryButton({ onClick, children }) {
    return (
        <button className='btn primary-btn' onClick={onClick}>{children}</button>
    )    
}

function SecondaryButton({ onClick, children }) {
    return (
        <button className='btn secondary-btn' onClick={onClick}>{children}</button>
    )
}

function DisabledButton({ children }) {
    return (
        <button className='disabled-btn btn' disabled>{children}</button>
    )
}

export {
    PrimaryButton,
    SecondaryButton,
    DisabledButton
}