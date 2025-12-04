import type {NextConfig} from "next";

const nextConfig: NextConfig = {
    output: "standalone",
    experimental: {
        turbopackMinify: false,
        serverMinification: false,
    }
};

export default nextConfig;
