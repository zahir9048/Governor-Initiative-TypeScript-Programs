export const metadata = {
  title: 'Next.js',
  description: 'Generated by Next.js',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body style={{backgroundColor: "red"}}>
        <header><h2>This is Public Page Header</h2></header>
        {children}
        <footer><h2>This is Public Page Footer</h2></footer>
      </body>
    </html>
  )
}
